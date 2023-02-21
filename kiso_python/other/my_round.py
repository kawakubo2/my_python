# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:26:18 2017

@author: tomok
"""

from math import ceil, floor, pow

def my_ceil(num, keta):
    temp = num * pow(10, keta)
    temp = ceil(temp)
    temp = temp / pow(10, keta)
    return temp
    
def my_floor(num, keta):
    temp = num * pow(10, keta)
    temp = floor(temp)
    temp = temp / pow(10, keta)
    return temp

def my_floor2(num, keta):
    return floor(num * pow(10, keta)) / pow(10, keta)

number1 = 2.425353
print(my_ceil(number1, 2))
print(my_floor(number1, 2))
print(my_floor2(number1, 2))