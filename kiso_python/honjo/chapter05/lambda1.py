# -*- coding: utf-8 -*-

addition = lambda x, y: x + y
subtract = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y

def mod(x, y):
    return x % y

ope_dict = {"+": addition, "-": subtract, "*": multiplication, "/": division, "%": mod }

operator = input("加減乗除を選択してください 加算->+, 減算->-, 乗算->*, 除算->/, 剰余->% :")
a = int(input("1番目の整数値: "))
b = int(input("2番目の整数値: "))
 
print("{}{}{}={}".format(a, operator, b, ope_dict[operator](a, b)))

# 関数の引数が関数、または関数の戻り値が関数---> 高階関数(higher order function)
def arithmetic(func, x, y):
    return func(x, y)

print(arithmetic(multiplication, 8, 7))

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(sum_even(numbers))

def sum_positive_odd(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 != 0:
            total += n
    return total

print(sum_positive_odd(numbers))

def mysum(func, nums):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print(mysum(lambda x: x > 0 and x % 2 != 0, numbers))

result = sum([n for n in numbers if n > 0 and n % 2 != 0])
print(result)