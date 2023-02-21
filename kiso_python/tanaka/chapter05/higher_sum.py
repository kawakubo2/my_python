numbers = [4, -3, 2, 1, -2, 6, 4, 7, 8]

def my_sum(nums):
    total = 0
    for n in nums:
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

def even_sum(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(even_sum(numbers))

def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(positive_even_sum(numbers))

def higher_sum(func, nums):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print(higher_sum(lambda n: n > 0, numbers))
print(higher_sum(lambda n: n % 2 == 0, numbers))
print(higher_sum(lambda n: n > 0 and n % 2 == 0, numbers))