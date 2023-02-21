# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:44:50 2017

@author: tomok
"""

try:
    score = int(input('点数を入力してください: '))
    if score >= 80:
        print('合格です')
    else:
        print('不合格です')
except ValueError as e:
    print('整数値を入力してください')
    print(e)
