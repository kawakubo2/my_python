# -*- coding: utf-8 -*-

import math

menseki = lambda hankei: hankei * hankei * math.pi

radius = 10
print('半径: {} -> 面積: {:.3f}'.format(radius, menseki(radius)))