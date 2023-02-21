# -*- coding: utf-8 -*-

nums1 = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum1(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum1(nums1))

def sum2(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

print(sum2(nums1))

def sum3(numbers):
    total = 0
    for n in numbers:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(sum3(nums1))

# 高階関数(higher order function)
def higher_sum(numbers, func):
    total = 0
    for n in numbers:
        if func(n):
            total += n
    return total

def positive_even(num):
    return num > 0 and num % 2 == 0

print(higher_sum(nums1, positive_even))

print(higher_sum(nums1,
    lambda num: num > 0 and num % 2 == 0))

print(higher_sum(nums1,
    lambda num: num > 0 and num % 2 == 0 and num % 3 != 0))

average = lambda *nums: sum(nums) / len(nums)

print(average(1, 10, 100))