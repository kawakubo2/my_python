colors = {'red', 'green', 'blue'}

colors.add('orange')
print(colors)
colors.add('red')
print(colors)
colors.remove('red')
print(colors)
colors.clear()
print(colors)

words1 = {'空', '海', '川', '地球'}
words2 = {'山', '海', '空', '空気'}

# 和集合
print(words1 | words2)

# 積集合
print(words1 & words2)

# 差集合
print(words1 - words2)

# 
print(words1 ^ words2)

a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {1, 3, 5, 7, 9}

# bはaの部分集合
print(b.issubset(a))

is_subset_flag = True
for n in b:
    if n not in a:
        is_subset_flag = False
if is_subset_flag:
    print('bはaの部分集合である')

s = "日月火水木金土"

weekdays = [c + "曜日" for c in s]
print(weekdays)

weekdays2 = []
for c in s:
    weekdays2.append(c + '曜日')

print(weekdays2)

import math
radius = [1, 2, 3, 4, 5, 6]
circle_areas = [r ** 2 * math.pi for r in radius]
print(circle_areas)