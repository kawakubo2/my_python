# -*- coding: utf-8 -*-

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def positive_even(nums):
    for n in nums:
        if n > 0 and n % 2 == 0:
            yield n
        
def circle_area(gen):
    import math
    for r in gen:
        yield r ** 2 * math.pi
        
total = 0
for area in circle_area(positive_even(numbers)):
    total += area
    
print(total)

print('--- 検算用 ---')

for area in circle_area(positive_even(numbers)):
    print(area)