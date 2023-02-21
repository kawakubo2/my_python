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
    
start = time.time()    
for n in random_gen(10000):
    continue
    # print('{} '.format(n), end='')
    
end = time.time()

print('処理時間:{}'.format(end - start))

def random_ng_gen(num):
    randoms = list(range(num))
    while True:
        if len(randoms) == 0:
            break
        else:
            n = random.choice(randoms)
            randoms.remove(n)
            yield n
        
    
start = time.time()    
for n in random_ng_gen(10000):
    continue
    #print('{} '.format(n), end='')
    
end = time.time()

print('処理時間:{}'.format(end - start))