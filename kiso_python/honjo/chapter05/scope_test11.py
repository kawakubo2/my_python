# -*- coding: utf-8 -*-

import scope_test10
from scope_test10 import sum_even
from scope_test10 import total as s_total
nums = [1, 5, 2, 4, 8]

total = scope_test10.sum1(nums)

print(scope_test10.total)
print(total)

print(sum_even(nums))
print(s_total)

print(1, 2, 3, 4, 5, 6, 7)
print(1, 2, 3, 4, 5, 6, 7, sep="-")

def sum1(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(sum1(5, 2, 3, 7))
print(sum1())

