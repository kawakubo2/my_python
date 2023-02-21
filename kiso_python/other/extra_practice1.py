# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 22:28:34 2017

@author: tomok
"""

import sys

age = int(input('年齢を入力してください: '))
gender = int(input('性別を入力してください　1:男性、2:女性 : '))

if age < 0:
    print('年齢は0以上で入力してください')
    sys.exit(-1)

if gender != 1 and gender != 2:
    print('性別は1まはた2で入力してください')
    sys.exit(-1)

if gender == 1:
    if age <= 20:
        print('2400円です')
    elif age <= 50:
        print('2800円です')
    elif age <= 70:
        print('3200円です')
    else:
        print('3600円です')        
else: 
    if age <= 20:
        print('20000円です')
    elif age <= 50:
        print('2200円です')
    elif age <= 70:
        print('2400円です')
    else:
        print('2600円です')   

print('---< 別解 >---')
if gender == 1 and age <= 20:
    print('2400円です')
elif gender == 1 and age <= 50:
    print('2800円です')
elif gender == 1 and age <= 70:
    print('3200円です')
elif gender == 1 and age > 70:
    print('3600円です')
elif gender == 2 and age <= 20:
    print('2000円です')
elif gender == 2 and age <= 50:
    print('2200円です')
elif gender == 2 and age <= 70:
    print('2400円です')
elif gender == 2 and age > 70:
    print('2600円です')
