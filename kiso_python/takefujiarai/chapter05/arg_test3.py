# -*- coding: utf-8 -*-

def test2(lst):
    print('lst: {}'.format(id(lst)))
    lst[0] = 0
    lst.append(100)
    print('lst: {}'.format(id(lst)))
    lst = [10, 20, 30]
    print('lst: {}'.format(id(lst)))
    lst[0] = 1000
    
list1 = [1, 2, 3]
print('list1: {}'.format(id(list1)))
test2(list1)
print(list1)

def zeros(lst):
    for i in range(len(lst)):
        lst[i] = 0
        
list2 = [1, 2, 3]
zeros(list2)
print(list2)
    
list3 = [1, 2, 3, 4, 5]

def multiplyBy(lst, n):
    for i in range(len(lst)):
        lst[i] *= n

print('list3:', end='')
print(list3)

multiplyBy(list3, 3)
print('list3:', end='')
print(list3)

def mysum(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(mysum(1, 2, 3, 4))

print(sum([1, 2, 3, 4]))
print(sum([1, 2, 3, 4]))

def triangle_area(base, height):
    return base * height / 2

print(triangle_area(10, 5))
print(triangle_area(height=8, base=12))

def print_even_sum(*numbers, desc):
    print('------< {} >------'.format(desc))
    total = 0
    for n in numbers:
        if n % 2 == 0:
            print(str(n) + ' ', end='')
            total += n
    print('\n------ 合計 ------')
    print(total)
    
print_even_sum(1, 2, 3, 4, 5, desc='1から5までの偶数の合計')

def print_positive_sum(desc, *numbers):
    print('------< {} >------'.format(desc))
    total = 0
    for n in numbers:
        if n > 0:
            print(str(n) + ' ', end='')
            total += n
    print('\n------ 合計 ------')
    print(total)
    
print_positive_sum('正の整数の合計', -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8)

import collections
Person = collections.namedtuple('Person', 'name age address')
arai = Person('荒井', 25, '千葉県太平洋側')
print(arai)

def average(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)

print(average(1, 10, 100))

print(sum([1, 2, 3, 4]))

print()