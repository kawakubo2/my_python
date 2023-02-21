# -*- coding: utf-8 -*-

nums1 = [8, 7, 13, 41, 81, 18, 15, 19, 5]
nums2 = [n for n in nums1 if n % 3 == 0]

print(nums2)

scores = [83, 18, 48, 72, -1, 100, 92, 130, 61]

total = sum([n for n in scores if 0 <= n <= 100])
print(total)

