# This is a sample Python script.

def seir(y, t, n, beta, gamma, delta):
    s, e, i, r = y
    dsdt = -beta * s * i / n
    dedt = beta * s * i / n - delta * e
    didt = delta * e - gamma * i
    drdt = gamma * i
    return dsdt, dedt, didt, drdt

def seird(y, t, n, beta, gamma, delta, alpha, rho):
    s, e, i, r, d = y
    dsdt = -beta * s * i / n
    dedt = beta * s * i / n - delta * e
    didt = delta * e - (1 - alpha) * gamma * i - alpha * rho * i
    drdt = (1 - alpha) * gamma * i
    dddt = alpha * rho * i
    return dsdt, dedt, didt, drdt, dddt

# def seird2(y, t, n, beta, gamma, delta, alpha, rho):
#     s, e, i, r, d = y
#     dsdt = -beta(t) * s * i / n
#     dedt = beta(t) * s * i / n - delta * e
#     didt = delta * e - (1 - alpha) * gamma * i - alpha * rho * i
#     drdt = (1 - alpha) * gamma * i
#     dddt = alpha * rho * i
#     return dsdt, dedt, didt, drdt, dddt
#
# def r_0(t):
#     return 5.0 if t < t else 0.8
# def beta(t):
#     return r_0(t) * gamma

# def deriv(y, t, n, beta, gamma, delta, alpha_opt, rho):
#     s, e, i, r, d = y
#     def alpha(t):
#         return s * i/n + alpha_opt
#
#     dsdt = -beta(t) * s * i / n
#     dedt = beta(t) * s * i / n - delta * e
#     didt = delta * e - (1 - alpha(t)) * gamma * i - alpha(t) * rho * i
#     drdt = (1 - alpha(t)) * gamma * i
#     dddt = alpha(t) * rho * i
#     return dsdt, dedt, didt, drdt, dddt
#
# def logistic_r_0(t):
#     return (r_ini-r_end) / (1 + np.exp(-k*(-t+xm))) + r_end

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from scipy.integrate import odeint
    import numpy as np
    import matplotlib.pyplot as plt

 #1) seir Model
    # n = 1000000
    # d = 4.0  # número de dias que uma pessoa propaga a doença
    # gamma = 1.0 / d
    # delta = 1.0 / 5.0  # (periodo de incubação 5 dias)
    # r_0 = 5.0  # também definido como beta/gama, é o valor total de pessoas infectadas
    #         # por uma unica pessoa.
    #
    # beta = r_0 * gamma
    # s0, e0, i0, r0 = n - 1, 1, 0, 0
    # t = np.linspace(0, 99, 100)
    # y0 = s0, e0, i0, r0
    #
    # out = odeint(seir, y0, t, args=(n, beta, gamma, delta))
    # s, e, i, r = out.T
    #
    # plt.plot(t, s, label='S')
    # plt.plot(t, e, label='E')
    # plt.plot(t, i, label='I')
    # plt.plot(t, r, label='R')
    # plt.legend()
    # plt.show()

