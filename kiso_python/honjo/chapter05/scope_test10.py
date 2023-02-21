# -*- coding: utf-8 -*-

total = 10

def sum1(nums):
    total = 0
    for n in nums:
        total += n
    return total

def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

