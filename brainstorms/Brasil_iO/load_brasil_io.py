#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:11:59 2020
função para leitura dos dados covid19 disponibilizado pelo
portal Brasil IO para uma cidade ou estado.
Para

@author: akel

"""
import requests
import numpy as np
from datetime import datetime


def read_city(cidade,estado):
    if cidade == 0:
        url='https://brasil.io/api/dataset/covid19/caso_full/data?city=&city_ibge_code=&date=&format=json&is_last=&place_type=state&search=&state='+ estado
    else:
        url='https://brasil.io/api/dataset/covid19/caso_full/data?city='+cidade+'&city_ibge_code=&date=&format=json&is_last=&place_type=city&search=&state='+ estado

#    url_state='https://brasil.io/api/dataset/covid19/caso_full/data?city=&city_ibge_code=&date=&format=json&is_last=&place_type=state&search=&state='+ estado
    r = requests.get(url)
    data = r.json()
    
    NL=len(data['results'])
    C=np.zeros(NL); 
    D=np.zeros(NL);
    NC=np.zeros(NL);
    ND=np.zeros(NL);
    C100=np.zeros(NL);
    date=np.zeros(NL,dtype=datetime);
    for i in range(NL):
        C[i]=data['results'][i]['last_available_confirmed'] 
        D[i]=data['results'][i]['last_available_deaths']   
        NC[i]=data['results'][i]['new_confirmed']
        ND[i]=data['results'][i]['new_deaths']
        C100[i]=data['results'][i]['last_available_confirmed_per_100k_inhabitants']
        data_str=data['results'][i]['last_available_date']
        date[i]=datetime.strptime(data_str,'%Y-%m-%d')
    return np.flipud(C),np.flipud(D),np.flipud(NC),np.flipud(ND),np.flipud(C100),np.flipud(date)
