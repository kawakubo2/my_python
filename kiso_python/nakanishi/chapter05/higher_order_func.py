nums = [5, 2, -3, 1, 4, -2, 9, 8, 7, 6]

def positive_total(numbers):
    total = 0
    for n in numbers:
        if n > 0:
            total += n
    return total

print(f"正数の合計: {positive_total(nums)}")

def even_total(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total

print(f"偶数の合計: {even_total(nums)}")

def positive_odd_total(numbers):
    total = 0
    for n in numbers:
        if n > 0 and n % 2 != 0:
            total += n

    return total

print(f"正の基数の合計: {positive_odd_total(nums)}")

def my_total(func, numbers):
    total = 0
    for n in numbers:
        if func(n):
            total += n
    return total

answer1 = my_total(lambda num: num > 0, nums)
print(f"正数の合計: {answer1}")
answer2 = my_total(lambda num: num % 2 == 0, nums)
print(f"偶数の合計: {answer2}")
answer3 = my_total(lambda num: num > 0 and num % 2 != 0, nums)
print(f"正の奇数の合計: {answer3}")