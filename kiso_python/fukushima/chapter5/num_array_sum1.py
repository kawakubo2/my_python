# -*- coding: utf-8 -*-

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

def my_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

def my_positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

def my_positive_odd_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 != 0:
            total += n
    return total

def higher_sum(func, nums):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print('全合計: {}'.format(my_sum(numbers)))
print('全合計: {}'.format(higher_sum(lambda n: True, numbers)))
print('正数の合計: {}'.format(my_positive_sum(numbers)))
print('正数の合計: {}'.format(higher_sum(lambda n: n > 0, numbers)))
print('正数の奇数の合計: {}'.format(my_positive_odd_sum(numbers)))
print('正数の奇数の合計: {}'.format(higher_sum(lambda n: n > 0 and n % 2 != 0, numbers)))