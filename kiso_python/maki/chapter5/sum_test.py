# -*- coding: utf-8 -*-

def sum1(nums):
    total = 0
    for n in nums:
        total += n
    return total

def sum2(nums):
    total =  0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

def sum3(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

def sum4(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 1:
            total += n
    return total

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('合計:', sum1(numbers))
print('偶数の合計:', sum2(numbers))
print('プラスの合計:', sum3(numbers))
print('プラスの奇数の合計:', sum4(numbers))

# 高階関数
def super_sum(nums, func):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total
            
def even(n):
    return n % 2 == 0

def positive(n):
    return n > 0

def positive_odd(n):
    return n > 0 and n % 2 == 1

print('---< super_sum >---')
print('偶数の合計',super_sum(numbers, even))
print('プラスの合計',super_sum(numbers, positive))
print('プラスの奇数の合計',super_sum(numbers, positive_odd))

print('プラスの奇数の合計',super_sum(numbers, lambda n: n > 0 and n % 2 == 1))


