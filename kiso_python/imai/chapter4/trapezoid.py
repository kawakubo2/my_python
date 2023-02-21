# -*- coding: utf-8 -*-

# trapezoid.py

import sys

if len(sys.argv) != 4:
    print('使用法: python3 trapezoid.py 上底 下底 高さ')
    print('例 python3 trapezoid.py 5.2 4.8 6.0')
    sys.exit(-1)
    
upperbase = float(sys.argv[1]) # 上底
lowerbase = float(sys.argv[2]) # 下底
height    = float(sys.argv[3]) # 高さ

area = (upperbase + lowerbase) * height / 2

print("上底が{}cm、下底が{}cm、高さが{}cmの台形の面積は{}平方cmです。", format(
        upperbase, lowerbase, height, area))
    