# -*- coding: utf-8 -*-
import math

while True:
    try:
        radius = float(input('半径を入力してください: '))
    except ValueError:
        print('数値の形式に誤りがあります')
    else:
        area = math.pow(radius, 2) * math.pi
        print("半径が{:.1f}cmの円の面積は{:.1f}平方cmです。".format(radius, area))
        break
        

