#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:24:03 2020

@author: akel

Programa Realiza plotagem de dados obtidos
da sespa-pa e de simulações do modelo SIR A

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

# #leitura de dados
mat_cont = spio.loadmat('covidpara24.mat')
mat_str=mat_cont['res']
mat_str.shape
val = mat_str[0,0]

#atribuição das variaveis
d0=np.concatenate(val['date0'])
C=np.concatenate(val['C'])
Ce=np.concatenate(val['Ce'])
dif=np.concatenate(val['dif'])
dt=0.1
Ca=np.concatenate(val['Ca'])
k=val['day']
dRMSE=np.concatenate(val['dRMSE'])
RMSE=np.concatenate(val['RMSE'])
sim=np.diff(Ca)/dt

tp0=val['tp0'];
tp1=val['tp1'];
tp2=val['tp2'];
tp3=val['tp3'];
tp4=val['tp4'];
tpend5=val['tpend5'];
tpend=val['tpend'];

k=datestr2num(tp2[0])

# ##definição do intervalo de tempo(dados - diferencia)
formatter = DateFormatter('%d/%m/')
dat1 = datetime.date(2020, 2, 11);
dat2 = datetime.date(2020, 5, 24);
delta0 = datetime.timedelta(days=1)
# #0.09844
dates0 = drange(dat1, dat2, delta0)


##definição do intervalo de tempo(dados - diferencia)
dat1 = datetime.date(2020, 2, 10);
dat2 = datetime.date(2020, 5, 24);
delta1 = datetime.timedelta(days=1)
#0.09844
dates1 = drange(dat1, dat2, delta1)



#definição do intervalo de tempo(simulacao difirenca)
# date1 = datetime.date(2020, 2, 11);
# date2 = datetime.date(2020, 6, 28);#date2-date1-->151 dias
# delta2 = datetime.timedelta(days=138.05/np.size(sim))
# dates2 = drange(date1, date2, delta2)

date1 = pd.Timestamp('2020-02-11')
date2= pd.Timestamp('2020-6-28')
t = np.linspace(date1.value, date2.value, np.size(sim))
dates_sim = pd.to_datetime(t)


print(np.size(sim))
print(np.size(dates_sim))

#definição do intervalo de tempo(simulacao total)
t = np.linspace(date1.value, date2.value, np.size(Ca))
dates_sim2 = pd.to_datetime(t)


maxsim=np.max(sim)
imaxsim=np.argmax(sim)
maxsum= np.round(np.sum(sim[0:imaxsim])/10)
temp=dates_sim[imaxsim]
datamax=temp.strftime("%d/%m")




fig, ax = plt.subplots(figsize=(19.20,10.80))

fig.canvas.set_window_title('Casos diarios')

ax.bar(dates0,np.diff(C),label='Dados( casos diarios)')
ax.plot(dates_sim,sim,'k',label='simulacão')
ax.plot(dates_sim,sim - dRMSE,'r--')
ax.plot(dates_sim,sim + dRMSE,'r--')
ax.fill_between(dates_sim, sim - dRMSE, sim + dRMSE, alpha=0.2)
ax.xaxis.set_major_formatter(formatter)
plt.ylim(0,1100)
plt.xlim(pd.Timestamp('2020-03-15'),pd.Timestamp('2020-06-15'))
plt.grid('major')
ax.set_ylabel('Novos Casos')
plt.legend()

#anotações
ax.annotate('Máximo número de casos ' + datamax + '\n total = '+ str(int(np.round(maxsim))),
            xy=(dates_sim[imaxsim], 834), xycoords='data',
            xytext=(-15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom',fontsize=14)

#título
fig.suptitle('Simulação SIR covid-19 estado do Pará', fontsize=14)
plt.title('Casos Diarios 24.05.2020 \n' + r'$R=1.4$ $\beta=0.987$ $\gamma=0.804$ $N=94296 $')

# plt.savefig('figuraa.png')    

#plt.savefig('/home/akel/Área de trabalho/image1.eps',format='eps',dpi=300,optimize=True)
# plt.savefig('/home/akel/Área de trabalho/image1.png',format='png',dpi=300)


# fig2, ax = plt.subplots()
# fig2.canvas.set_window_title('Casos totais')

# ax.plot(dates1,C,'bo',label='Dados',markersize=4)
# ax.plot(dates_sim2,Ca,'k',label='Simulacão')
# ax.plot(dates_sim2,Ca - 5*RMSE,'k--',lw=1)
# ax.plot(dates_sim2,Ca + 5*RMSE,'k--',lw=1)
# # #ax.fill_between(dates_sim2, Ca- 5*RMSE, Ca + 5*RMSE, color=[0.9 ,0.4,0.0],alpha=0.3)

# ax.xaxis.set_major_formatter(formatter)
# Max_casos = np.max(Ca)
# ax.axhline(Max_casos, color='green', lw=2,ls='--')
# xx=[dates_sim2[0],dates_sim2[imaxsim]]
# ax.plot(xx,[maxsum,maxsum],'k--',lw=2)
# ax.plot([dates_sim2[imaxsim],dates_sim2[imaxsim]],[0,maxsum],'k--',lw=2)
 
 
# ax.fill_between(dates_sim2, 0, 2, (dates_sim2>dates_sim2[1080]) & (dates_sim2<dates_sim2[np.size(sim)-1]),
#                 color=[0.0,1.0,0.0], alpha=0.4, transform=ax.get_xaxis_transform(),zorder=0)
# ax.fill_between(dates_sim2, 0, 2, (dates_sim2>dates_sim2[920]) & (dates_sim2<dates_sim2[1080]),
#                 color=[1.0,0.6,0.0], alpha=0.4, transform=ax.get_xaxis_transform(),zorder=0)
# ax.fill_between(dates_sim2, 0, 2, (dates_sim2>=dates_sim2[620]) & (dates_sim2<dates_sim2[920]),
#                   color=[1.0,0.0,0.0], alpha=0.4, transform=ax.get_xaxis_transform(),zorder=0)

# #anotações
# ax.annotate('Total de casos em '  + datamax + '\n'  +str(int(maxsum)),
#             xy=(dates_sim2[imaxsim], 12374), xycoords='data',
#             xytext=(-15, 25), textcoords='offset points',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             horizontalalignment='right', verticalalignment='bottom',fontsize=14)

# ax.set_ylabel('Total de infectados',fontsize=14)


# plt.xlim(date1,date2)
# plt.ylim(0,28000)
# plt.legend()
# plt.grid(True)

# # #titulo
# fig2.suptitle('Simulação SIR covid-19 estado do Pará', fontsize=14)
# plt.title('Casos totais 24.05.2020 \n' + r'$R=1.4$ $\beta=0.987$ $\gamma=0.804$ $N=94296 $')

plt.show()


