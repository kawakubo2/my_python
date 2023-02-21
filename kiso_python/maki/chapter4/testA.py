# -*- coding: utf-8 -*-

numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(numbers)):
    if (numbers[i] > 0 and numbers[i] % 2 == 1):
        print(numbers[i] * numbers[i])
        
for n in numbers:
    if n > 0 and n % 2 == 1:
        print(n * n)
        
positive_square = [n * n for n in numbers if n > 0 and n % 2 == 1]
for n in positive_square:
    print(n)