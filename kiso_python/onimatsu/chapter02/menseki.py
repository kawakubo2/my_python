# -*- coding: utf-8 -*-

import math

hankei = float(input('半径を入力してください: '))

menseki = math.pi * math.pow(hankei, 2)
print('半径が' + str(hankei) + 'の円の面積は' + str(menseki))

print('半径が{}の円の面積は{:.2f}'.format(hankei, menseki))
