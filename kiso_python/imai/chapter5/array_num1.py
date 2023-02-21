# -*- coding: utf-8 -*-

# array_sum1.py

numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def my_sum(nums):
    total = 0
    for n in nums:
        if True:
            total += n
    return total

print(my_sum(numbers))

def positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print(positive_sum(numbers))

def positive_odd_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 != 0:
            total += n
    return total

print(positive_odd_sum(numbers))

# 高階関数(higher order function)
def higher_sum(func, nums):
    """
    func:整数値を引数に取り、戻る値として真偽値型を返す
    nums:は整数のリスト
    戻り値:funcの条件がTrueの整数の合計
    """
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print(higher_sum(lambda n: n > 0, numbers))
print(higher_sum(lambda n: n > 0 and n % 2 != 0, numbers))