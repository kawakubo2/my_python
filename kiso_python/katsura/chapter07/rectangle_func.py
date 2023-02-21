# Rectangle(長方形)
import math

def area(width, height): 
    return width * height

def diagonal(width, height):
    return math.hypot(width, height)

def perimeter(width, height):
    return (width + height) * 2

w = 8
h = 5
print(f'幅が{h}、高さが{w}の長方形の面積は{area(w, h)}')
print(f'幅が{h}、高さが{w}の長方形の対角線は{diagonal(w, h)}')
print(f'幅が{h}、高さが{w}の長方形の外周の長さは{perimeter(w, h)}')