# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:13:57 2017

@author: tomok
"""

print('2つの整数値の積を計算します')
while True:
    try:
        x = int(input('整数値(x)を入力してください: '))
        break
    except ValueError:
        print('形式に誤りがあります')
        
while True:
    try:
        y = int(input('整数値(y)を入力してください: '))
        break
    except ValueError:
        print('形式に誤りがあります')

print('x*y=' + str(x * y))

