# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    sys.exit(-1)
    
upper_base = float(sys.argv[1])
lower_base = float(sys.argv[2])
height     = float(sys.argv[3])
area = (upper_base + lower_base) * height / 2

print('上底が{:.1f}cm、下底が{:.1f}cm、高さが{:.1f}cmの台形の面積は{:.1f}平方cmです'\
      .format(upper_base, lower_base, height, area))