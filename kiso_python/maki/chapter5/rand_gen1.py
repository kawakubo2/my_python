# -*- coding: utf-8 -*-

import random

def random_gen(num):
    
    randoms = []
    
    while True:
        rand_num = random.randrange(num)
        
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break
        
rand = random_gen(10)
print(next(rand))
print(next(rand))
print(next(rand))
print(next(rand))
print(next(rand))