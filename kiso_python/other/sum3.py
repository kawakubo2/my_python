# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:32:47 2017

@author: tomok
"""

numbers = [4, 2, 1, 4, 5, 8, 7, 1, 10]

counter = 0
sum = 0
while counter < len(numbers):
    if sum + numbers[counter] >= 10:
        break
    sum += numbers[counter]
    counter += 1

print("配列の最初の5個の要素の合計は", sum)