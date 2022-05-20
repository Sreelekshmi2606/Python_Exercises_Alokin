# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:26:31 2022

@author: Sreelu
"""

name= input('Enter your name: ')
Empid=input('Enter your employee id: ')
basic=int(input('Enter your basic pay: '))

if basic >10000:
    print('HRA is',0.15*basic)
    print('DA is',0.8*basic)
if basic >=5000 and basic<10000:
    print('HRA is',0.10*basic)
    print('DA is',0.5*basic)
if basic<5000:
    print('HRA is',0.5*basic)
    print('DA is',0.3*basic)