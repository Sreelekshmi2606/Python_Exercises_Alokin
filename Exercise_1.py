# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:42:11 2022

@author: Sreelu
"""

Math=int(input('Enter maths mark: '))
Chem=int(input('Enter chemistry marks: '))
Eng= int(input('Enter English mark: '))
Phy=int(input('Enter Physics mark: '))
IT=int(input('Enter It mark: '))
Bio=int(input('Enter Biology mark: '))
Total=Math+Chem+Eng+Phy+IT+Bio
print('Total mark is ',Total)
Averag= Total/6
print('Total average is',round(Averag,2))
if Averag >=90:
    print('A grade')
elif Averag >=70 and Averag<90:
    print('B garde')
elif Averag >=50 and Averag<70:
    print('C garde')
else:
    print('Failed')