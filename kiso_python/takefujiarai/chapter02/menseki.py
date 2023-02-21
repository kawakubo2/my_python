# -*- coding: utf-8 -*-

from math import pow, pi

hankei = float(input('半径を入力してください:'))

menseki = pi * pow(hankei, 2)

print('半径が' + str(hankei) + 'の円の面積 → ' + str(menseki))
