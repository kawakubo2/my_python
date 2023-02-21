# -*- coding: utf-8 -*-

import math

def menseki(hankei):
    return hankei ** 2 * math.pi

radius = 10
print("半径: {} -> 面積: {:.3f}".format(radius, menseki(radius)))