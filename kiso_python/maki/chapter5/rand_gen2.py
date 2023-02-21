# -*- coding: utf-8 -*-

import random
import time

def random_gen(num):
    
    randoms = set()
    
    while True:
        rand_num = random.randrange(num)
        
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break
        
rg = random_gen(30000)
start = time.time()
for r in rg:
    print(r)
end = time.time()
print('処理時間:', end - start)