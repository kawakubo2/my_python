numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum1(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(f"合計: {sum1(numbers)}")

def even_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print(f"正数の合計: {even_sum(numbers)}")

def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(f"正の偶数の合計: {positive_even_sum(numbers)}")

def higher_sum(func, nums):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

def add(x, y):
    return x + y

add2 = lambda a, b: a + b

print(add2(30, 20))

print(f"正の偶数の合計: {higher_sum(lambda n: n > 0 and n % 2 == 0, numbers)}")

def is_positive_even(num):
    return num > 0 and num % 2 == 0

print(f"正の偶数の合計: {higher_sum(is_positive_even, numbers)}")

def my_filter(func, nums):
    result = []
    for n in nums:
        if func(n):
            result.append(n)
    return result
    
list2 = my_filter(lambda n: n % 2 == 0, numbers)

print(list2)

