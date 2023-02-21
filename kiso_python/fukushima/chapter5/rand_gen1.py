# -*- coding: utf-8 -*-

import random
import time

def random_gen(num):
    
    used_nums = set()
    
    while True:
        rand_num = random.randrange(num)
        if rand_num not in used_nums:
            used_nums.add(rand_num)
            yield rand_num
        elif len(used_nums) == num:
            break

start = time.time()
for n in random_gen(100000):
    pass
end = time.time()

print('処理時間: {:.3f}'.format(end - start))