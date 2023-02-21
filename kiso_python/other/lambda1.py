# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:00:49 2017

@author: tomok
"""

numbers = [1, 2, 3, 4, 5, 6, 7]


def sum(lst, func):
    total = 0
    for n in lst:
        if(func(n)):
            total += n
    return total

print(sum(numbers, lambda n: n % 2 != 0))


