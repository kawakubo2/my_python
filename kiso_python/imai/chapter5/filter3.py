# -*- coding: utf-8 -*-

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = [inch * 2.54 for inch in inches if inch > 5]
print(cms)

cms2 = []
for cm in map(lambda n: n * 2.54, filter(lambda n: n > 5, inches)):
    cms2.append(cm)
print(cms2)