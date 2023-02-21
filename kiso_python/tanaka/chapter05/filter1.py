def to_cm(inch):
    return inch * 2.54

def larger_5(inch):
    return inch > 5

inches = [9, 5.5, 4, 6, 5, 6.5, 10]

cms = []
#
# 関数の引数として関数を受け取るものを高階関数
#
for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
    
print(cms)

cms2 = []
for inch in inches:
    if inch > 5:
        cms2.append(inch * 2.54)
print(cms2)

cms3 = [inch * 2.54 for inch in inches if inch > 5]
print(cms3)

cms4 = []
for cm in map(to_cm, filter(larger_5, inches)):
    cms4.append(cm)