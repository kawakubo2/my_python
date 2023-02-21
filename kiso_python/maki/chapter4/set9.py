# -*- coding: utf-8 -*-

numbers = [101, 102, 103, 101, 101, 110, 105, 103, 101, 108, 102]

pure_numbers = set()
for n in numbers:
    pure_numbers.add(n)
    
for n in pure_numbers:
    print(n)
    
print('-----')
pure_numbers2 = set(numbers)
for n in pure_numbers2:
    print(n)