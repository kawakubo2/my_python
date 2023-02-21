# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:33:03 2017

@author: tomok
"""

numbers = [1, 2, 4, 8, 16, 32]

def my_sum(num_array):
    sum = 0
    for n in num_array:
        sum = sum + n
    return sum

print(my_sum(numbers))