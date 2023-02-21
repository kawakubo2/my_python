# -*- coding: utf-8 -*-

nums = [73, 39, 78, 58, 92, 88, 100, 98, 62, 49 ]

avg = sum(nums) / len(nums)

var1 = sum([(num - avg) ** 2 for num in nums]) / len(nums)

print('分散:', var1, ' 標準偏差:', var1 ** 0.5)