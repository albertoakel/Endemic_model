#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:02:59 2021

@author: akel
"""


import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
from matplotlib.dates import num2date,datestr2num
import numpy as np
import datetime
import pandas as pd
import scipy.io as spio
  
plt.close('all')

t = np.logspace(0,11, 10000)
No=100
T=np.array([1.39*10E10,4.5E9,1.3E9])
NN=np.zeros((10000,len(T)))
fig, ax = plt.subplots(figsize=(19.20,10.80))

for i in range(0,len(T),1):
    lamb=np.log(2)/T[i]
    N=No*np.exp(-lamb*t)
    NN[0:10000,i]=N
   

ax.plot(t,NN[:,0],label='Th232',lw=4)
ax.plot(t,NN[:,1],label='U238',lw=4)
ax.plot(t,NN[:,2],label='K40',lw=4)


plt.xlabel('Tempo [Anos]',size=18)
plt.ylabel('N',size=18)
plt.yticks(np.arange(0, 101, 10))
plt.xticks(np.array([0E9,1E9,1.3E9,2E9,3E9,4E9,4.5E9,6E9,7E9,8E9,9E9,10E10]))

plt.xticks(size=14)
plt.grid('major')
plt.xlim(1,10000000000)
plt.legend()
plt.show()


#plt.savefig('/home/akel/Documentos/pos-doc UFPA/disciplinas/físicadaterra/Aulas/aula 7 - geofisica prospecçao/figura.png',format='png',dpi=300,optimize=True)





