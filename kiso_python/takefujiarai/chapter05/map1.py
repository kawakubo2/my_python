# -*- coding: utf-8 -*-

def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]

for cm in map(to_cm, inches):
    print(cm)
    
print('---< lambda式 >---')
cms = list(map(lambda inch: inch * 2.54, inches))
print(cms)
    
print('---< リストの内包表記 >---')
cms = [inch * 2.54 for inch in inches]
print(cms)

def larger_5(inch):
    return inch > 5

cms = []

for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
    
print(cms)

cms = []
for inch in filter(lambda inch: inch > 5, inches):
    cms.append(inch * 2.54)
print(cms)

cms = [inch * 2.54 for inch in inches if inch > 5]
print(cms)

cms = []
for cm in map(to_cm, filter(larger_5, inches)):
    cms.append(cm)
print(cms)