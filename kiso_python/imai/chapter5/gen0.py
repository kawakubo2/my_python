# -*- coding: utf-8 -*-

numbers = [5, 12, -3, 9, 8, 10, -2, 7, 38, 15, 20]

def positive_filter(numbers):
    for n in numbers:
        if n > 0:
            yield n
            
def even_filter(gen):
    for n in gen:
        if n % 2 == 0:
            yield n
            
def circle_area(gen):
    import math
    for n in gen:
        yield(n ** 2 * math.pi)
            
            
for area in circle_area(even_filter(positive_filter(numbers))):
    print(area)