# -*- coding: utf-8 -*-

# 高階関数(higher order function)

numbers = [-3, -2 -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

def mysum(nums):
    """
    引数 nums: 整数のリスト
    戻り値: リストの合計
    """
    total = 0
    for n in nums:
        total += n
    return total

help(mysum)

print('--- 単純に合計を求める ---')
print('合計:', mysum(numbers))

def positive_sum(nums):
    """
    引数 nums: 整数のリスト
    戻り値: 引数のリストのうち正の整数だけの合計
    """
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print('--- 正の整数の合計を求める ---')
print('正の整数の合計:', positive_sum(numbers))

def positive_odd_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 != 0:
            total += n
    return total

print('--- 正の奇数の合計を求める ---')
print('正の奇数の合計:', positive_odd_sum(numbers))

#
def higher_sum(nums, func):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

def positive_num(n):
    return n > 0

print('正の整数の合計:', higher_sum(numbers, positive_num))

def positive_odd_num(n):
    return n > 0 and n % 2 != 0

print('正の奇数の合計:', higher_sum(numbers, positive_odd_num))

print('正の奇数の合計:', higher_sum(numbers, lambda n: n > 0 and n % 2 != 0))
    