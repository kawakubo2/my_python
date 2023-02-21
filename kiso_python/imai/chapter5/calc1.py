# -*- coding: utf-8 -*-

total = 0

def add(x):
    global total
    total += x # total = total + x
    
def sub(x):
    global total
    total -= x
    
add(100)
sub(50)
add(30)

print('total =', total)

print('わたしは', 'Pythonを勉強して', 30, '年以上になる')
print()

def my_sum(*nums):
    print(type(nums))
    total = 0
    for n in nums:
        total += n
    return total

print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))