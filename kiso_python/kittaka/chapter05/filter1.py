def larger_5(inch):
    return inch > 5

def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = []
for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
print(cms)

cms2 = []
for cm in map(to_cm, filter(larger_5, inches)):
    cms2.append(cm)
print(cms2)

cms3 = [inch * 2.54 for inch in inches if inch > 5]
print(cms3)