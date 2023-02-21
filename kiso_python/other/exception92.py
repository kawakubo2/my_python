# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:55:19 2017

@author: tomok
"""

try:
    score = int(input('点数を入力してください: '))
except:
    print('整数値を入力してください')
else:
    print('入力した点数:', score)
    if (score >= 80):
        print('合格です')
    else:
        print('不合格です')