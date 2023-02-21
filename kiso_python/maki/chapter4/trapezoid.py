# -*- coding: utf-8 -*-

# trapezoid ---> 台形
# python3 trapezoid.py 5.2 4.8 5.0

import sys

if len(sys.argv) != 4:
    print('引数不正')
    sys.exit(-1)
    
upperbase = float(sys.argv[1])
lowerbase = float(sys.argv[2])
height    = float(sys.argv[3])

area = (upperbase + lowerbase) * height / 2

print('上底{}、下底{}、高さ{}の台形の面積は{}です。'\
      .format(upperbase, lowerbase, height, area))