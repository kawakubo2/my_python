# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:44:24 2017

@author: tomoharu
"""

def gen_prime(max_num):
    num = 2
    while num <= max_num:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

for n in gen_prime(29):
    print(n)
