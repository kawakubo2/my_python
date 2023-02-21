# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:16:28 2017

@author: tomok
"""

import math

num = float(input('数値を入力してください: '))
print(str(num) + 'の平方根: ', math.sqrt(num))
print("{0}の平方根は{1:.3f}".format(num, math.sqrt(num)))
