# -*- coding: utf-8 -*-

nums = [99, 3, -5, 0, 100, 14, 18, 14]
print('---< sort前 >---')
print(nums)
nums.sort()
print('---< 昇順にソート後 >---')
print(nums)
nums.sort(reverse=True)
print('---< 降順にソート後 >---')
print(nums)

nums = [99, 3, -5, 0, 100, 14, 18, 14]
nums2 = sorted(nums, reverse=True)
print(nums)
print(nums2)


