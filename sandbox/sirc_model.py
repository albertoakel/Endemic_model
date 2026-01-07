from scipy.integrate import odeint
import numpy as np

def SIRC(y, t, N, beta, gamma):
    S, I, R, C = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    dCdt = beta * S * I / N
    return [dSdt, dIdt, dRdt, dCdt]

def solve_sirc(t, N, beta, gamma, I0):
    R0 = 0
    C0 = I0
    S0 = N - I0 - R0
    y0 = [S0, I0, R0, C0]
    sol = odeint(SIRC, y0, t, args=(N, beta, gamma))
    return sol[:, 3]

def initial_SIRC(C):
    """
        Estima os parâmetros iniciais da curva logística usando 3 pontos dos dados C.

        input:
        C : array-like

        Output:
        [K, r, A] ou None
        """
    C = np.array(C)
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

        C1, C2, C3 = C[k1], C[k2], C[k3]

        q = C2 ** 2 - C3 * C1
        if q <= 0:
            continue
        p = C1 * C2 - 2 * C1 * C3 + C2 * C3
        if p <= 0:
            continue

        K = C2 * p / q

        try:
            r = np.log((C3 * (C2 - C1)) / (C1 * (C3 - C2))) / m
        except (ZeroDivisionError, ValueError):
            continue
        if r < 0:
            continue

        try:
            A = ((C3 - C2) * (C2 - C1) / q) * \
                ((C3 * (C2 - C1)) / (C1 * (C3 - C2))) ** ((k3 - m) / m)
        except (ZeroDivisionError, ValueError):
            continue
        if A <= 0:
            continue

        return [K, r, A]

    return None
