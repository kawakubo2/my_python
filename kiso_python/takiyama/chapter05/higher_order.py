numbers = [-3, 5, 4, 2, 8, 7, -4, 6]

def total(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

sum1 = total(numbers)
print(f"合計: {sum1}")

def positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total
psum = positive_sum(numbers)
print(f"正数の合計: {psum}")

def even_sum(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total
esum = even_sum(numbers)
print(f"偶数の合計: {esum}")
    
def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total
pesum = positive_even_sum(numbers)
print(f"正の偶数の合計: {pesum}")

def higher_order_sum(filter, nums):
    total = 0
    for n in nums:
        if filter(n):
            total += n
    return total

def even(num):
    return num % 2 == 0

esum2 = higher_order_sum(even, numbers)
print(f"偶数の合計: {esum2}")

esum3 = higher_order_sum(lambda n: n % 2 == 0, numbers)
print(f"偶数の合計: {esum3}")

pesum2 = higher_order_sum(lambda n: n > 0 and n % 2 == 0, numbers)
print(f"正の偶数の合計: {pesum2}")