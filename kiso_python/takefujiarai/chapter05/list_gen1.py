# -*- coding: utf-8 -*-
import math

nums = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_positive_filter(numbers):
    for n in numbers:
        if n > 0 and n % 2 == 0:
            yield n

def circle_area(numbers):
    for n in numbers:
        yield n ** 2 * math.pi
            
for n in circle_area(even_positive_filter(nums)):
    print(n)
    
circle_areas = [r ** 2 * math.pi for r in nums if r > 0 and r % 2 == 0]
print(circle_areas)