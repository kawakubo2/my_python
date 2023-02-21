# -*- coding: utf-8 -*-

import sys

if len(sys.argv) != 4:
    print('使用法: python trapezoid.py 上底 下底 高さ')
    print('例: python trapezoid.py 4.8 5.2 5.0')
    sys.exit(-1)

upper_base = float(sys.argv[1])
lower_base = float(sys.argv[2])
height     = float(sys.argv[3])

area = (upper_base + lower_base) * height / 2

print("台形の面積は{}です。".format(area))
    
