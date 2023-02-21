# -*- coding: utf-8 -*-

import random, time

def rand_gen(num):
    
    # 生成済みの乱数を格納するリスト
    randoms = set()
    
    while True:
        rand_num = random.randrange(num)
        
        if rand＿num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break
        
start = time.time()
for r in rand_gen(200000):
    pass
print(time.time() - start)        

            