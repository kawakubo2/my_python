# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:45:31 2017

@author: tomok
"""

def average(*num):
    sum = 0
    for n in num:
        sum += n
    return sum / len(num)

print(average(1, 10, 100))
