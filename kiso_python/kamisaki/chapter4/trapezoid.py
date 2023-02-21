import sys

if len(sys.argv) != 4:
    print('使用法: python trapezoid.py 5.2 4.8 8.0')
    sys.exit()

upperbase = float(sys.argv[1])
lowerbase = float(sys.argv[2])
height    = float(sys.argv[3])

print(f"{(upperbase + lowerbase) * height / 2:.2f}")