# trapezoid.py
import sys

if len(sys.argv) != 4:
    print('引数は4個必要です。')
    sys.exit()

upperbase = float(sys.argv[1])
lowerbase = float(sys.argv[2])
height    = float(sys.argv[3])

print((upperbase + lowerbase) * height / 2)