# -*- coding: utf-8 -*-

inches = [9, 5.5, 6, 4, 5, 6.5, 10]

def larger_5(inch):
    return inch > 5

cms = []

for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
    
print(cms)
