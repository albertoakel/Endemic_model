#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:19:24 2020

@author: akel
Modelos epidemiologicos compartimentados
"""
import numpy as np

def SIR(y, t, N, beta, gamma):
    """
    Modelo SIR :
    - S: Suscetíveis
    - I: Infectados ativos
    - R: Recuperados
    """
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def SEIR(y, t, N, beta, alpha,gamma):
    """
    Modelo SEIR :
    - S: Suscetíveis
    - E: Exposto ( periodo de incubação)
    - I: Infectados ativos
    - R: Recuperados
    """
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - alpha * E
    dIdt = alpha * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

def SEIAR(y, t, N, beta, alpha, gamma_I, gamma_A, rho, kappa): 
    """
    Modelo SEIAR :
    - S: Suscetíveis
    - E: Exposto ( periodo de incubação)
    - I: Infectados ativos
    - A: Assintomático( contagioso sem sintoma)
    - R: Recuperados
    """
    S, E, I, A, R = y
    temp = (I+kappa*A)/N
    dSdt = -beta*S*temp
    dEdt = beta*S*temp-alpha*E
    dIdt = (1 - rho) * alpha * E - gamma_I * I
    dAdt = rho * alpha * E - gamma_A * A
    dRdt = gamma_I * I + gamma_A * A
    
    return [dSdt, dEdt, dIdt, dAdt, dRdt]


def SEIARD(y, t, N, beta, kappa, alpha, rho, gamma_I, gamma_A, delta_I):
    """
    Modelo SEIARD :
    - S: Suscetíveis
    - E: Exposto ( periodo de incubação)
    - I: Infectados ativos
    - A: Assintomático( contagioso sem sintoma)
    - R: Recuperados
    - D: Death(óbito)
    """
    S, E, I, A, R, D = y
    N_eff = N - D
    
    temp = beta * (I + kappa * A) / N_eff  # Força de infecção
    dSdt = -temp * S
    dEdt = temp* S - alpha * E
    dIdt = (1 - rho) * alpha * E - (gamma_I + delta_I) * I
    dAdt = rho * alpha * E - gamma_A * A
    dRdt = gamma_I * I + gamma_A * A
    dDdt = delta_I * I
    
    return [dSdt, dEdt, dIdt, dAdt, dRdt, dDdt]



def SIRC(y,t, N, beta, gamma):
    """
    Modelo SIR modificado que retorna:
    - S: Suscetíveis
    - I: Infectados ativos
    - R: Recuperados
    - C: Infectados acumulados (novo) (C=I+R)
    """
    S, I, R, C = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    dCdt = beta * S * I / N  # (derivada dos acumulados)
    return [dSdt, dIdt, dRdt, dCdt]

def SEIRC(y, t, N, beta, alpha,gamma):
    S, E, I, R, C = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - alpha * E
    dIdt = alpha * E - gamma * I
    dRdt = gamma * I
    dCdt = alpha*E
    return [dSdt, dEdt, dIdt, dRdt,dCdt]

def SEIARC(y, t, N, beta, alpha, gamma_I, gamma_A, rho, kappa): 
    """
    Modelo SEIRC :
    - S: Suscetíveis
    - E: Exposto ( periodo de incubação)
    - I: Infectados ativos
    - A: Assintomático( contagioso sem sintoma)
    - R: Recuperados
    """
    S, E, I, A, R,C = y
    temp = (I+kappa*A)/N
    dSdt = -beta*S*temp
    dEdt = beta*S*temp-alpha*E
    dIdt = (1 - rho) * alpha * E - gamma_I * I
    dAdt = rho * alpha * E - gamma_A * A
    dRdt = gamma_I * I + gamma_A * A
    dCdt = alpha*E
    
    return [dSdt, dEdt, dIdt, dAdt, dRdt,dCdt]

def SEIARDC(y, t, N, beta, kappa, alpha, rho, gamma_I, gamma_A, delta_I):
    """
    Modelo SEIARD :
    - S: Suscetíveis
    - E: Exposto ( periodo de incubação)
    - I: Infectados ativos
    - A: Assintomático( contagioso sem sintoma)
    - R: Recuperados
    - D: Death(óbito)
    """
    S, E, I, A, R, D, C = y  # Novo: C(t)
    
    # População ajustada (exclui óbitos)
    N_eff = N - D
    # Força de infecção
    temp = beta * (I + kappa * A) / N_eff  # Força de infecção
    
    # Equações
    dSdt = -temp* S
    dEdt = temp* S - alpha * E
    dIdt = (1 - rho) * alpha * E - (gamma_I + delta_I) * I
    dAdt = rho * alpha * E - gamma_A * A
    dRdt = gamma_I * I + gamma_A * A
    dDdt = delta_I * I
    dCdt = alpha * E  # Novos casos = fluxo E → I + E → A
    
    return [dSdt, dEdt, dIdt, dAdt, dRdt, dDdt, dCdt]

def SIR2(y, t, params):
    S, I, R = y
    N = params['N'].value
    beta = params['beta'].value
    gamma = params['gamma'].value
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


def SIRC2(C, t, N,beta, gamma, Io):
    """
    Modelo SIR simplificado em termos de C(t) — casos acumulados.

    Parâmetros:
    - C: número acumulado de casos no tempo t
    - t: tempo (não usado diretamente pois é autônomo)
    - beta: taxa de infecção
    - gamma: taxa de recuperação
    - N: população total
    - I0: número inicial de infectados

    Retorna:
    - dC/dt: derivada do número acumulado de casos
    """  
    i0 = Io / N
    c = C / N     
    dCdt = N * (1 - c) * (beta * c + gamma * np.log((1 - c + 1e-10) / (1 - i0 + 1e-10)))
    return dCdt


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

        q = C2**2 - C3 * C1
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
            A = ((C3 - C2)*(C2 - C1)/q) * \
                ((C3 * (C2 - C1)) / (C1 * (C3 - C2)))**((k3 - m)/m)
        except (ZeroDivisionError, ValueError):
            continue
        if A <= 0:
            continue

        return [K, r, A]

    return None