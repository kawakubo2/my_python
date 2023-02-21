# -*- coding: utf-8 -*-

numbers = [1, 2, [3, 4, [5, 6], 7], [8, [9, 10]]]

def list_sum(nums):
    if type(nums) != list:
        raise ValueError()
    sum = 0
    for n in nums:
        if type(n) == list:
            sum += list_sum(n)
        else:
            sum += n
    return sum

total = list_sum(numbers)
print('合計 =', total)