import math

def diagonal(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


width = 8 # 幅
height = 6 # 高さ
c = diagonal(width, height)
print(f"幅が{width}、高さが{height}の長方形の対角線は{c}です。")