import lmfit
from sirc_model import solve_sirc, initial_SIRC
import numpy as np

def ajustar_modelo(y):
    t = np.arange(len(y))
    K, r, A = initial_SIRC(y)

    I0 = K / (A + 1)
    N = 2 * K
    gamma_i = 2 * r
    beta_i = 1.5 * gamma_i

    # ---------------------------
    # PARÂMETROS INICIAIS
    # ---------------------------
    print('\n' + '=' * 40)
    print('PARÂMETROS INICIAIS'.center(40))
    print('=' * 40)
    print(f'{"I0:":<10}{I0:>30.6f}')
    print(f'{"N:":<10}{N:>30.6f}')
    print(f'{"gamma_i:":<10}{gamma_i:>30.6f}')
    print(f'{"beta_i:":<10}{beta_i:>30.6f}')

    model = lmfit.Model(solve_sirc, independent_vars=['t'])
    params = model.make_params()
    params['N'].set(value=N, vary=False)
    params['beta'].set(value=beta_i, min=0.001, max=3.0)
    params['gamma'].set(value=gamma_i, min=0.001, max=2.0)
    params['I0'].set(value=I0, vary=False)

    result = model.fit(y, params, t=t)
    return result, t
