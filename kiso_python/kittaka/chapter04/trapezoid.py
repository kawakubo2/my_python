import sys

if len(sys.argv) != 4:
    print("使用法: python trapezoid.py 上底 下底 高さ")
    print("使用例: python trapezoid.py 5.2 4.8 5.0")
    sys.exit()
    
upperbase = float(sys.argv[1])
lowerbase = float(sys.argv[2])
height    = float(sys.argv[3])
area = (upperbase + lowerbase) * height / 2
print(f"上底が{upperbase}、下底が{lowerbase}、高さが{height}の台形の面積は{area:.1f}")