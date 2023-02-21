# -*- coding: utf-8 -*-

nums = [99, 3, -5, 0, 100, 14, 18, 14]

print("sortメソッドは破壊的メソッドである")
print("sort前")
print(nums)

nums.sort()

print("sort後")
print(nums)

print("元のリストを保持してsortされた新しいリストが欲しい場合はsorted関数を使用する")
print("sorted関数は非破壊的")
nums1 = [99, 3, -5, 0, 100, 14, 18, 14]
nums2 = sorted(nums1)

print(nums1)
print(nums2)

str_list1 = ['Yamada', 'kato', 'Sato', 'Suzuki']
str_list2 = sorted([s.lower() for s in str_list1])
print(str_list2)