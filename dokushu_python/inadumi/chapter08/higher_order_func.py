numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def my_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(f"合計: {my_sum(numbers)}")

def positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print(f"正数の合計: {positive_sum(numbers)}")

def even_sum(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(f"偶数の合計: {even_sum(numbers)}")

def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(f"偶数の整数の合計: {positive_even_sum(numbers)}")

def higher_sum(func, nums):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total


def even(n):
    return n % 2 == 0

print(f"偶数の合計: {higher_sum(even, numbers)}")

print(f"正数の偶数の合計: {higher_sum(lambda n: n > 0 and n % 2 == 0, numbers)}")

x = 1.23456
import math
print(math.floor(x))
print(math.ceil(x))

def higher_round(x, func, prec):
    return func(x * (10 ** prec)) / (10 ** prec)

print(higher_round(x, math.floor, 2))
print(higher_round(x, math.ceil, 3))