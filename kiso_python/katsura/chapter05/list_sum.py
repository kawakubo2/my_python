numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def even_sum(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(f'偶数の合計: {even_sum(numbers)}')

def positive_odd_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 != 0:
            total += n
    return total

print(f'正の奇数の合計: {positive_odd_sum(numbers)}')

def positive_even_except_3nobaisu(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0 and n % 3 != 0:
            total += n
    return total

print(f'正の偶数のうち3の倍数を除いた合計: {positive_even_except_3nobaisu(numbers)}')

"""
高階関数(higher order function)とは、引数として関数を受け取ったり、戻り値として
関数を返す関数のこと。
"""

def higher_order_sum(filter, nums):
    """[summary]

    Args:
        filter function: 整数を引数に取り、戻り値としてbool型を返す関数
        nums 整数型のリスト: 合計を求める元となるリスト
    """
    total = 0
    for n in nums:
        if filter(n):
            total += n
    return total

print(f'偶数の合計: \
    {higher_order_sum(lambda n: n % 2 == 0, numbers)}')
print(f'正の奇数の合計: \
    {higher_order_sum(lambda n: n > 0 and n % 2 != 0, numbers)}')
print(f'正の偶数のうち3の倍数を除いた合計: \
    {higher_order_sum(lambda n: n > 0 and n % 2 == 0 and n % 3 != 0, numbers)}')

def positive_even(n):
    return n > 0 and n % 2 == 0

print(f'正の偶数の合計: {higher_order_sum(positive_even, numbers)}')