import math

def mul(x, y):
    return x * y

def square(x):
    return mul(x, x)

def hypot(x, y):
    if not (type(x) in (int, float) and type(y) in (int, float)):
        raise ValueError('引数が数値ではありません。')
    return math.sqrt(square(x) + square(y))

try:
    a = 'a'
    b = 8
    print(hypot(a, b))
except ValueError as e:
    print(e)