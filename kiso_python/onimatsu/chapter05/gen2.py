# -*- coding: utf-8 -*-

def my_gen1(str):
    for c in str.upper():
        yield c

gen = my_gen1('Hello')    
for c in gen:
    print(c)
    
def even_filter(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

def circle_area(nums):
    import math
    for n in nums:
        yield n ** 2 * math.pi
    
radius = [1, 2, 3, 4, 5, 6, 7, 8]

print('---< ジェネレータを使った場合 >---')
for a in circle_area(even_filter(radius)):
    print(a)

print('---< リストの内包表記を使った場合 >---')
import math
areas = [r ** 2 * math.pi for r in radius if r % 2 == 0]

for area in areas:
    print(area)