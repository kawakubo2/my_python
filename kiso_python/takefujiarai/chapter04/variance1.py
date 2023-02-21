# -*- coding: utf-8 -*-
import math

nums = [42, 46, 60, 67, 57, 72, 56, 58, 81, 50]

avg1 = sum(nums) / len(nums)

var1 = sum([(num - avg1) ** 2 for num in nums]) / len(nums)
print(var1)

print(var1 ** 0.5)

area_total = sum([r ** 2 * math.pi for r in nums])
print(area_total)

dolls = [1, 5, 9.5, 100]

rate = 101

yens = [doll * rate for doll in dolls]

print(yens)

weekdays = [day + '曜日' for day in '月火水木金土日']
print(weekdays)

height = [182, 167, 159, 172, 172]
weight = [81, 58, 61, 58, 68]

bmis = [w / ((h/100)**2) for h, w in zip(height, weight)]
print(bmis)