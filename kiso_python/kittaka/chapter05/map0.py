def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = []
for inch in inches:
    cm = to_cm(inch)
    cms.append(cm)

print(cms)

cms2 = list(map(to_cm, inches))
print(cms2)

for cm in map(to_cm, inches):
    print(cm)

print(type(map(to_cm, inches)))

import math

for sqrt in map(math.sqrt, inches):
    print(sqrt)

s = ["Python", "C", "Java", "PHP", "JavaScript"]

for slen in map(len, s):
    print(slen)