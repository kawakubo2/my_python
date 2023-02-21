import sys

if len(sys.argv) != 4:
    print('引数の数が違います。')
    print('使用法: python trapezoid.py 上底 下底 高さ')
    print('例: python trapezoid.py 7.3 2.7 10.0')
    sys.exit()

try:
    upperbase = float(sys.argv[1])
    lowerbase = float(sys.argv[2])
    height    = float(sys.argv[3])
    print((upperbase + lowerbase) * height / 2)
except:
    print('数値を入力してください')