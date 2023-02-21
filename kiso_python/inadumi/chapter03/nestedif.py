# -*- coding: utf-8 -*-
import sys

gender = int(input('性別を入力してください 1.女性 2.男性 :'))
if gender != 1 and gender != 2:
    print('性別は1または2を入力してください')
    sys.exit(-1)

age = int(input('年齢を入力してください:'))
if age < 0:
    print('年齢は0以上を入力してください')
    sys.exit(-2)
    
if gender == 1: # 女性
    if age <= 20:
        price = 2000
    elif age <= 50:
        price = 2200
    elif age <= 70:
        price = 2400
    else:
        price = 2600
else: # 男性
    if age <= 20:
        price = 2400
    elif age <= 50:
        price = 2800
    elif age <= 70:
        price = 3200
    else:
        price = 3600

        
print('{}円です'.format(price))
    


