# -*- coding: utf-8 -*-

import sys

# python trapezoid.py 5.2 4.8 5.0
if len(sys.argv) != 4:
    print("使用法:python trapezoid.py 上底 下底 高さ")
    print("使用例:python trapezoid.py 5.2 4.8 5.0")
    sys.exit(-1)

# 上底
upper_base = float(sys.argv[1])
lower_base = float(sys.argv[2])
height     = float(sys.argv[3])

area = (upper_base + lower_base) * height / 2

print("上底が{:.2f}cm、下底が{:.2f}cm、高さが{:.2f}cmの台形の面積は{:.2f}平方cmです"
       .format(upper_base, lower_base, height, area))
