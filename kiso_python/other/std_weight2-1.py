# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:24:01 2017

@author: tomok
"""

import math

height = float(input('身長(cm)で入力してください: '))

bmi = 22

std_weight = bmi * (height / 100) ** 2
print('身長: ' + str(height) + 'cm -> ', end='')
#print('標準体重: ' + str(math.floor(std_weight)) + 'kg')
print("標準体重: {:.1f}kg".format(std_weight))
