numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def my_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

print('合計:{}'.format(my_sum(numbers)))

def postive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print('正数の合計:{}'.format(postive_sum(numbers)))

def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print('正の偶数の合計:{}'.format(positive_even_sum(numbers)))

def higher_sum(func, nums):
    '''
    func: 整数値を引数に取りbool型を返す関数
    nums: 整数のリスト
    '''
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print('正の偶数の合計:{}'.format(higher_sum(lambda n: n > 0 and n % 2 == 0, numbers)))

def postive_even(n):
    return n > 0 and n % 2 == 0

print('正の偶数の合計:{}'.format(higher_sum(postive_even, numbers)))

