import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# =============================================================================
# Função principal: ajusta o modelo SIR aos dados
# =============================================================================

def fit_virus(get_data, **kwargs):
    # -------------------------------------------------------------------------
    # Parâmetros padrão
    Nmax = 12e6
    plot_results = kwargs.get('plt', True)
    max_iter = kwargs.get('maxit', None)
    day_limit = kwargs.get('day', None)
    w1 = kwargs.get('w1', None)
    w2 = kwargs.get('w2', None)

    # -------------------------------------------------------------------------
    # Carrega os dados
    country, C, date0 = get_data()
    C = np.array(C)
    original_C = C.copy()
    original_date0 = date0

    # Aplica limite de dias se especificado
    if day_limit is not None:
        C = C[:day_limit]

    # Verifica crescimento dos dados
    n0 = 0
    for i in range(1, len(C)):
        if C[i] < C[i - 1]:
            raise ValueError(f'Dados inválidos: C({i}) < C({i-1})')
        if C[i] == C[i - 1]:
            n0 = i
            date0 += timedelta(days=1)
        else:
            break

    if len(C[n0:]) <= 5:
        print(f'Dados insuficientes para {country}')
        return None

    C = C[n0:]

    # -------------------------------------------------------------------------
    # Estimativa inicial com curva logística
    b0 = initial_guess(C)
    if b0 is None:
        print(f'Falha ao obter chute inicial para {country}')
        return None

    K0, r, A = b0
    I0 = K0 / (A + 1)
    N = 2 * K0
    gamma = 2 * r
    beta = 1.5 * gamma

    # Vetor de tempo
    days = len(C)
    t = np.arange(days)

    # Define os pesos se não foram fornecidos
    if w1 is None and w2 is None:
        weight_options = [(1, 0), (0, 1), (1, 1)]
    else:
        weight_options = [(w1 or 1, w2 or 0)]

    best_result = None
    best_obj = np.inf

    for w1_test, w2_test in weight_options:
        x0 = [beta, gamma, N, I0]
        bounds = [(1e-6, None), (1e-6, None), (1e3, Nmax), (1.0, Nmax)]

        result = minimize(
            objective_function,
            x0,
            args=(C, t, w1_test, w2_test),
            bounds=bounds,
            method='L-BFGS-B',
            options={'maxiter': max_iter or 10000, 'disp': False}
        )

        if result.success and result.fun < best_obj:
            best_result = result
            best_obj = result.fun
            w1_final, w2_final = w1_test, w2_test

    if best_result is None:
        print(f'Falha na otimização para {country}')
        return None

    beta, gamma, N, I0 = best_result.x
    R0 = beta / gamma

    # =============================================================================
    # Simulação com os parâmetros otimizados
    # =============================================================================

    t_extended = np.linspace(0, len(C) + 60, 500)
    Ca = odeint(sir_ode, I0, t_extended, args=(beta, gamma, N, I0)).flatten()
    Ce = odeint(sir_ode, I0, t, args=(beta, gamma, N, I0)).flatten()
    next_day_forecast = Ca[len(C)]

    # =============================================================================
    # Estatísticas: R², RMSE
    # =============================================================================

    residuals = C - Ce
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((C - np.mean(C))**2)
    r2 = 1 - ss_res / ss_tot
    rmse = np.sqrt(ss_res / (len(C) - 1))

    # =============================================================================
    # Casos diários e pico da epidemia
    # =============================================================================

    daily_C = np.diff(C)
    daily_Ce = np.diff(Ce)
    daily_forecast = np.diff(Ca)

    tm_index = np.argmax(daily_Ce)
    tm_day = t[tm_index]
    tm_date = date0 + timedelta(days=int(tm_day))

    tend_index = np.where(daily_forecast < 1)[0]
    tend_day = int(t_extended[tend_index[0]]) if len(tend_index) > 0 else int(t_extended[-1])
    tend_date = date0 + timedelta(days=tend_day)

    # =============================================================================
    # Gráficos
    # =============================================================================

    if plot_results:
        dates = [date0 + timedelta(days=int(i)) for i in range(len(C))]
        forecast_dates = [date0 + timedelta(days=int(i)) for i in t_extended]

        # Casos acumulados
        plt.figure(figsize=(10, 6))
        plt.plot(forecast_dates, Ca, label='Previsão (modelo)', linewidth=2)
        plt.scatter(dates, C, label='Dados reais', color='black', zorder=5)
        plt.plot(dates, Ce, '--', label='Ajuste', linewidth=2)
        plt.xlabel('Data')
        plt.ylabel('Casos acumulados')
        plt.title(f'Epidemia em {country} (Modelo SIR)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=30)
        plt.show()

        # Casos diários
        daily_dates = [date0 + timedelta(days=int(i)) for i in t[1:]]
        plt.figure(figsize=(10, 4))
        plt.bar(daily_dates, daily_C, label='Casos reais (diários)', color='gray')
        plt.plot(daily_dates, daily_Ce, label='Previsão (diários)', linewidth=2)
        plt.xlabel('Data')
        plt.ylabel('Novos casos por dia')
        plt.title(f'Evolução diária - {country}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=30)
        plt.show()

    # =============================================================================
    # Resultado
    # =============================================================================

    result = {
        'country': country,
        'R0': R0,
        'beta': beta,
        'gamma': gamma,
        'N': N,
        'I0': I0,
        'data': C,
        'fit': Ce,
        'forecast_curve': Ca,
        'next_day_forecast': next_day_forecast,
        'w1': w1_final,
        'w2': w2_final,
        'fmin': best_obj,
        'Ce': Ce,
        'daily_C': daily_C,
        'daily_Ce': daily_Ce,
        'R2': r2,
        'RMSE': rmse,
        'peak_day': int(tm_day),
        'peak_date': tm_date.strftime('%Y-%m-%d'),
        'end_day': tend_day,
        'end_date': tend_date.strftime('%Y-%m-%d'),
    }

    return result

# =============================================================================
# Funções auxiliares
# =============================================================================

def sir_ode(C, t, beta, gamma, N, I0):
    c0 = I0 / N
    c = C / N
    dCdt = N * (1 - c) * (beta * c + gamma * np.log((1 - c) / (1 - c0)))
    return dCdt

def objective_function(params, C, t, w1, w2):
    beta, gamma, N, I0 = params
    try:
        sol = odeint(sir_ode, I0, t, args=(beta, gamma, N, I0)).flatten()
    except Exception:
        return np.inf
    if np.any(np.isnan(sol)):
        return np.inf

    c1 = w1 / (w1 + w2)
    c2 = w2 / (w1 + w2)
    f1 = np.linalg.norm(C - sol)
    f2 = np.linalg.norm(np.diff(C) - np.diff(sol))
    return c1 * f1 + c2 * f2

def initial_guess(C):
    n = len(C)
    if n <= 5:
        return None
    for i in range(n - 5):
        k1 = i
        k3 = n - 1
        k2 = (k1 + k3) // 2
        m = k2 - k1
        if m < 1 or any(np.isnan(C[[k1, k2, k3]])):
            continue
        q = C[k2] ** 2 - C[k3] * C[k1]
        if q <= 0:
            continue
        p = C[k1] * C[k2] - 2 * C[k1] * C[k3] + C[k2] * C[k3]
        if p <= 0:
            continue
        K = C[k2] * p / q
        try:
            r = np.log((C[k3] * (C[k2] - C[k1])) / (C[k1] * (C[k3] - C[k2]))) / m
        except:
            continue
        if r < 0:
            continue
        A = ((C[k3] - C[k2]) * (C[k2] - C[k1]) / q) * \
            ((C[k3] * (C[k2] - C[k1])) / (C[k1] * (C[k3] - C[k2]))) ** ((k3 - m) / m)
        if A <= 0:
            continue
        return [K, r, A]
    return None
