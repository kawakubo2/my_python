numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def my_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

def positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

def higher_sum(nums, filter):
    total = 0
    for n in nums:
        if filter(n):
            total += n
    return total

print('配列全体の合計:{}'.format(my_sum(numbers)))
print('配列全体の合計:{}'.format(higher_sum(numbers, lambda n: True)))
print('正数の合計:{}'.format(positive_sum(numbers)))
print('正数の合計:{}'.format(higher_sum(numbers, lambda n: n > 0)))
print('正偶数の合計:{}'.format(positive_even_sum(numbers)))
print('正偶数の合計:{}'.format(higher_sum(numbers, lambda n: n > 0 and n % 2 == 0)))