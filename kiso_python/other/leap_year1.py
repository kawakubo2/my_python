# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:21:05 2017

@author: tomok
"""

year = int(input('年の値を入力してください: '))

if ((year % 4 == 0) and (year % 100 != 0)) \
    or (year % 400 == 0):
    print('閏年です')
else:
    print('閏年ではありません')