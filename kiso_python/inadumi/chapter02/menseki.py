# -*- coding: utf-8 -*-

import math

hankei = float(input('半径を入力してください:'))

menseki = math.pi * math.pow(hankei, 2)

print('半径{}の円の面積は{}'.format(hankei, menseki))

def menseki(hankei):
    return math.pi * math.pow(hankei, 2)

print(menseki(9))