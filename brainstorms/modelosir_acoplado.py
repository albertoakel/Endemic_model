#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:49:19 2020

@author: akel
Modelo Sir acoplado aos dados

"""

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
from datetime import datetime               
import numpy as np
import matplotlib.dates as mdates
from scipy.integrate import odeint

import lmfit
from lmfit.lineshapes import gaussian, lorentzian
import warnings

import modelos_epidemiologicos as model


#import requests
import sys
#sys.path.insert(1, '/home/akel/programaspythoncovid')
import load_brasil_io as ld

# from .programaspythoncovid.load_brasil_io import read_city


plt.close('all')
cidade='Belém' # Primeira letra Maiuscula e com acentuação
estado='PA' #sigla do estado maiuscula

out=ld.read_city(0, estado) 
C,D,NC,ND,C100,date=out

t0=np.linspace(0,70,70)

plt.plot(t0,np.cumsum(NC[0:70]),'-o')
dados=np.cumsum(NC[0:70])


# #simulação SIR
N = 200000


#beta = 0.036
D = 12 #número de dias que uma pessoa propaga a doença
gamma = 1.0 / D
#gamma=0.335
R_0=2.3
beta = R_0 * gamma 
print('beta',beta)
print('gamma',gamma)
I0=3
S0=N-I0
R0 =0
t = np.linspace(0, 70,70) 
y0 = S0, I0, R0 
out = odeint(model.SIR, y0, t, args=(N, beta, gamma))
S, I, R = out.T

print(len(I))
plt.plot(t0,np.cumsum(I),label='I',color='r')

plt.ylim((0,28000))



def SIRMODEL(nt,beta,gamma):
#    gamma=1.0/D
#    beta=R_0*gamma
    S0=204998-3
    y0 = S0, 3, 0
    t = np.linspace(0, 70, nt) 
    odeint(model.SIR, y0, t, args=(N, beta, gamma))
    S, I, R = out.T
    return I

mod = lmfit.Model(SIRMODEL) #atribuindo modelo

mod.set_param_hint("beta", value=0.1, vary=True, min=0.1, max=4.0) #
mod.set_param_hint("gamma", value=0.1, vary=True, min=0.1, max=2.0) #
params = mod.make_params()


t1=70
#Method:leastsq,brute,least_squares
SS = mod.fit(dados, params, method='least_squares', nt=t1,max_nfev=1000000)
print(SS.fit_report())
print(SS.values['beta'])
# plt.plot(t,R,label='R')
# plt.legend()


# ##SEIR MODEL
# N = 204998 
# D = 5              #número de dias que uma pessoa propaga a doença
# gamma = 1.0 / D 
# #gamma=0.335  
# delta = 1.0 / 4.5      #(periodo de incubação 5 dias)
# R_0 = 2.2              #também definido como beta/gama, é o valor total
#                         #de pessoas infectadas por uma unica pessoa.
# beta = R_0 * gamma 
# #beta=0.7



# E0=3
# SO=N-E0
# I0, R0 = 0, 0  
# t = np.linspace(0, 99, 1000) 
# y0 = S0, E0, I0, R0 

# out = odeint(model.SEIR, y0, t, args=(N, beta, gamma,delta))

# S,E, I, R = out.T

# plt.plot(t,np.cumsum(I),label='I',color='g')

# plt.xlim((0,80))
# plt.ylim((0,15000))



#inversão função logistica
# def logistica_model(t,L,k,xo):
#     return (L) / (1 + np.exp(-k*(t-xo)))



# mod = lmfit.Model(logistica_model) #atribuindo modelo

# #definindo parametros 

# mod.set_param_hint("L", value=10000.0, vary=True,min=10000, max=20000.0) #
# mod.set_param_hint("k", value=1.0, vary=True,min=0.0, max=1.0) #
# mod.set_param_hint("xo", value=1.0, vary=True,min=1., max=90.0) #


# params = mod.make_params()
# #t1 = np.linspace(0, 200.0,np1)
# #method:leastsq,brute
# out = mod.fit(C, params, method="least_squares", t=t,max_nfev=10000000)
# dely = out.eval_uncertainty(t=t,sigma=1)

# print(out.fit_report())

# b1=out.values['L']
# c1=out.values['k']
# d1=out.values['xo']
# t=t=np.linspace(0,185,86)
# f_fit=logistica_model(t,b1,c1,d1)
#plt.plot(t,f_fit,'--')