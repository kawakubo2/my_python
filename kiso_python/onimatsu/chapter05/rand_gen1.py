# -*- coding: utf-8 -*-

import random

def random_gen(num):
    
    randoms = []
    
    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield rand_num
        else:
            if len(randoms) == num:
                break

for n in random_gen(10):
    print(n)