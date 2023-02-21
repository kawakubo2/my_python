# -*- coding: utf-8 -*-

import math

def menseki(hankei):
    return hankei * hankei * math.pi

hankei = 10

print("半径: {} -> 面積:　{:.3f}".format(hankei, menseki(hankei)))