# -*- coding: utf-8 -*-

inches = [9, 5.5, 6, 5, 6.5, 10]

def to_cm(inch):
    return inch * 2.54

for cm in map(to_cm, inches):
    print(cm)
    
cms = list(map(to_cm, inches))
print(cms)

cms = [n * 2.54 for n in inches]
print(cms)


def larger_5(inch):
    return inch > 5

for inch in filter(larger_5, inches):
    print(inch * 2.54)
    
for cm in map(to_cm, filter(larger_5, inches)):
    print(cm)
    
for cm in map(lambda n: n * 2.54, 
              filter(lambda n: n > 5, inches)):
    print(cm)
    
for cm in [inch * 2.54 for inch in inches if inch > 5]:
    print(cm)