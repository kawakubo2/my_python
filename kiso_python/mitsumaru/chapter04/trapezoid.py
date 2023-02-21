# trapezoid.py

import sys

if len(sys.argv) != 4:
    print('使用法: python trapezoid.py 上底 下底 高さ')
    print('例: python trapoezoid.py 4.8 5.2 5.0')
    sys.exit()

upperbase = float(sys.argv[1]) # 上底
lowerbase = float(sys.argv[2]) # 下底
height    = float(sys.argv[3]) # 高さ

print((upperbase + lowerbase) * height / 2)
