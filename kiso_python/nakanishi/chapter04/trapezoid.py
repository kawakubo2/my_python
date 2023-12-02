import sys

if len(sys.argv) != 4:
    print("使用法 python trapezoid.py 上底 下底 高さ")
    print("使用例 python trapezoid.py 4.2 5.8 4.0")
    sys.exit(-1)

upperbase = float(sys.argv[1])
lowerbase = float(sys.argv[2])
height    = float(sys.argv[3])

print(f"上底が{upperbase}、下底が{lowerbase}、高さが{height}の台形の面積は{(upperbase + lowerbase) * height / 2}")