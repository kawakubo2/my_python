# -*- coding: utf-8 -*-

inches = [9, 5.5, 6, 4, 5, 6.5, 10]

cms = []

for inch in filter(lambda n: n > 5, inches):
    cms.append(inch * 2.54)
    
print(cms)