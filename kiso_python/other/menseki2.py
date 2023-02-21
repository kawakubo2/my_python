# -*- coding: utf-8 -*-

import math

hankei = float(input('半径を入力してください: '))

menseki = math.pi * math.pow(hankei, 2)
print("半径が{}cmの円の面積は{:.3f}平方cmです。".format(hankei, menseki))
