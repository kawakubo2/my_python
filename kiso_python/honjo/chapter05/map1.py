# -*- coding: utf-8 -*-

def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]

for cm in map(to_cm, inches):
    print(cm)

print('------------------')
for cm in map(lambda inch: inch * 2.54, inches):
    print(cm)
    
radius = [5, 4.5, 3, 10]

import math

def circle_area(r):
    return r ** 2 * math.pi

for area in map(circle_area, radius):
    print(area)
    
areas = [r ** 2 * math.pi for r in radius]
print(areas)
    
cms = [inch * 2.54 for inch in inches]
print(cms)