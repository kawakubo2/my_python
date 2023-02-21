# -*- coding: utf-8 -*-
"""
Created on Fri May  5 20:29:45 2017

@author: tomok
"""

# 再帰メソッド
def rec_sum(numbers):
    sum = 0
    for item in numbers:
        if isinstance(item, list):
            sum += rec_sum(item)
        else:
            sum += item
    
    return sum

num_array = [1, 2, [3, 4, 5, [6, 7], 8, 9, [10]]]
print(rec_sum(num_array))


