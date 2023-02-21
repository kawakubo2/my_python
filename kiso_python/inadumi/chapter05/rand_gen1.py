# -*- coding: utf-8 -*-

import random, time

def random_gen(num):
    
    randoms = []
    
    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.append(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break

start_time = time.time()
rand = random_gen(100000)
for n in rand:
    pass
end_time = time.time()
print(end_time - start_time)
    