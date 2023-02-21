# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate):
    return doll * rate

yen = doll_to_yen(100, 105)
print("為替レート: {}".format(105))
print("{}ドルは{}円".format(100, yen))

rate = 100
doll = 150

yen = doll_to_yen(doll, rate)
print("為替レート: {}".format(rate))
print("{}ドルは{}円".format(doll, yen))

yen = doll_to_yen(rate = 101, doll=200)
print("為替レート: {}".format(101))
print("{}ドルは{}円".format(200, yen))

def trapezoid_area(upperbase, lowerbase, height):
    return (upperbase + lowerbase) * height / 2;


print(trapezoid_area(4, height = 3, lowerbase = 5))