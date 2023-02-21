# -*- coding: utf-8 -*-

words1 = {'空', '海', '川', '地球'}
words2 = {'山', '海', '空', '空気'}

print(words1 | words2)
print(words1 & words2)
print(words1 - words2)
print(words1 ^ words2)

num1 = { -3, -2,  -1, 0, 1, 2, 3, 4, 5, 6, 7 }
num2 = {1, 2, 3, 4, 5 }


print(set.issuperset(num1, num2))
print(set.issubset(num2, num1))

def is_subset(nums1, nums2):
    for n in nums2:
        if n not in nums1:
            return False
    return True

print(is_subset(num1, num2))
        