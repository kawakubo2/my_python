# -*- coding: utf-8 -*-

import math

menseki = lambda hankei: hankei * hankei * math.pi

hankei=10

print('半径: {}-> 面積: {:.3f}'.format(hankei, menseki(hankei)))