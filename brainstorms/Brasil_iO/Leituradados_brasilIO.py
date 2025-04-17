#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:01:55 2020

@author: akel
"""
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
from datetime import datetime               
import numpy as np
import requests
import load_brasil_io as ld

plt.close('all')
cidade='Florianópolos' # Primeira letra Maiuscula e com acentuação.
estado='SC' #sigla do estado maiuscula

#Para gerar informação apenas do estado, coloque cidade=0
out=ld.read_city(cidade, estado)
C,D,NC,ND,C100,date=out #casos, morte, casos diario, mortes diarias, caso 100k


##Para Plotar
formatter = DateFormatter('%d/%m/')    
fig, ax = plt.subplots(figsize=(19.20,10.80))
ax.plot(date,C,'-o',label=cidade+'-'+estado)
ax.xaxis.set_major_formatter(formatter)
plt.xlim(pd.Timestamp(date[71]),pd.Timestamp(date[-1]))

plt.legend()
plt.grid(True,zorder=0)



##Descomentar para salvar com datas
# filename='covid19.'+str(cidade)+'.'+estado+'.dat'
# f=open(filename,'w')
# for i in range(len(C)):
#     f.write('{0:5} {1:5d} {2:5d} {3:5d} {4:5d} {5:4.5F} \n'.format(date[i].strftime("%d-%m-%Y"),int(C[i]),int(NC[i]),int(D[i]),int(ND[i]),C100[i]))
           
# f.close()


##Descomentar para salvar sem datas
# filename='covid19.'+str(cidade)+'.'+estado+'.dat'
# f=open(filename,'w')
# for i in range(len(C)):
#     f.write('{0:5d} {1:5d} {2:5d} {3:5d} {4:4.5F} \n'.format(int(C[i]),int(NC[i]),int(D[i]),int(ND[i]),C100[i]))            
# f.close()
