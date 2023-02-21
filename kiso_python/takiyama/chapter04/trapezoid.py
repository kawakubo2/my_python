# trapezoid.py
import sys

if len(sys.argv) != 4:
    print("引数の数が違います。")
    print("使用法: python trapezoid.py 上底 下底 高さ")
    print("例: python trapezoid 4.8 5.2 4.0")
    sys.exit()
    
_, upperbase, lowerbase, height = sys.argv
area = (float(upperbase) + float(lowerbase)) * float(height) / 2
print(f"台形の面積: {area}")

area = (float(sys.argv[1]) + float(sys.argv[2])) * float(sys.argv[3]) / 2
print(f"台形の面積: {area}")

print(type(sys.argv))