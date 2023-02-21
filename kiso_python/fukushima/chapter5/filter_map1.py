# -*- coding: utf-8 -*-
from math import pow, pi

nums = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def area(r):
    return pow(r, 2) * pi

def positive_even(n):
    return n > 0 and n % 2 == 0

for circle_area in map(lambda r:pow(r, 2) * pi, filter(lambda n: n > 0 and n % 2 == 0, nums)):
    print(circle_area)
    
    
for circle_area in [ pow(r, 2) * pi for r in nums if r > 0 and r % 2 == 0]:
    print(circle_area)