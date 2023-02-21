# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:13:34 2017

@author: tomok
"""

import math

hankei = float(input("半径を入力してください:　"))
menseki = math.pi * math.pow(hankei, 2)
print("半径が{}の円の面積は{:.2f}".format(hankei, menseki))
