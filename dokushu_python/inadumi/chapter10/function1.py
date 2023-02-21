import math

def getRectangleArea(width, height):
    return width * height

def getDiagonal(width, height):
    return math.hypot(width, height)

def getPerimeter(width, height):
    return (width + height) * 2

def getTrinangle(base, height):
    return base * height / 2

w = 8
h = 6
print(f'長方形の面積: {getRectangleArea(w, h)}')
print(f'長方形の対角線の長さ: {getDiagonal(w, h)}')
print(f'長方形の外周の長さ: {getPerimeter(w, h)}')