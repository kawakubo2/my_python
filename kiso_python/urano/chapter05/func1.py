# func1.py
import math

def add(x, y):
    return x + y

a = 100
b = 200
c = add(a, b)
print(f"{a}+{b}={c}")

def price_with_tax(price, tax_rate):
    return math.floor(price * (1 + tax_rate))

rate = 0.08
price = 1000
print(f"税込み金額: {price_with_tax(price, rate)}")

"""
["Python", "Java", "PHP", "JavaScript"]
Python
Java
PHP
JavaScript
"""
def print_list(lst):
    for elem in lst:
        print(f"{elem} ", end="")
    print()

lang = ["Python", "Java", "PHP", "JavaScript"]
print_list(lang)
numbers = [100, 150, 70, 200, 120]
print_list(numbers)

def total(nums):
    result = 0
    for n in nums:
        result += n
    return result

print(f"合計: {total(numbers)}")

"""
1Lあたり162円、25.7Lの料金は
calc_charge(162, 25.7) ---> 4163
"""
def calc_charge(price_for_litter, litter):
    return math.floor(price_for_litter * litter)

p = 162
l = 25.7
print(f"1Lあたり{p}円です。{l}Lの料金は{calc_charge(p, l)}円となります。")

"""
sub(100, 70) ---> 30
"""
def sub(x, y):
    return x - y;

a = 100
b = 70
print(f"{a}-{b}={sub(a, b)}")

def mul(x, y):
    return x * y

a = 10
b = 30
print(f"{a}*{b}={mul(a, b)}")

def div(x, y):
    return x / y

a = 100
b = 3
print(f"{a}/{b}={div(a, b)}")