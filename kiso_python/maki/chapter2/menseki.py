# -*- coding: utf-8 -*-

import math

def circle_area(hankei):
    return math.pi * math.pow(hankei, 2)

hankei = float(input('半径を入力してください: '))

print('半径が' + str(hankei) + 'の円の面積 → ' + str(circle_area(hankei)))