# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate):
    return doll * rate

yen = doll_to_yen(100, 105)
print('為替レート: {}'.format(105))
print('{}ドルは{}円'.format(100, yen))

r = 100
d = 150
yen = doll_to_yen(d, r)
print('為替レート: {}'.format(r))
print('{}ドルは{}円'.format(d, yen))

yen = doll_to_yen(rate = 110, doll = 200)
print('為替レート: {}'.format(110))
print('{}ドルは{}円'.format(200, yen))

def trapezoid_area(upperbase, lowerbase = 50, height = 100):
    return (upperbase + lowerbase) * height / 2

print(trapezoid_area(100, 200))
print(trapezoid_area(100))

def circle_area(radius = 100):
    import math
    return math.pow(radius, 2) * math.pi

print(circle_area())