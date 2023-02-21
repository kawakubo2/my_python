# -*- coding: utf-8 -*-

import math

def even_filter(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
            
def sqr(gen):
    for n in gen:
        yield n ** 2

def mul_pi(gen):
    for n in gen:
        yield n * math.pi

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in mul_pi(sqr(even_filter(numbers))):
    print(n)

print('---< ジェネレータ式 >---')   
for circle_area in (n * math.pi for n in (n ** 2 for n in (n for n in numbers if n % 2 == 0))):
    print(circle_area)