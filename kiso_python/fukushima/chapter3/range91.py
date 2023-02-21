# -*- coding: utf-8 -*-

import time



# 1から10億までに存在する317の倍数

print('---< 解法1 >---')
start = time.time()

total = 0
for n in range(1, 1000000001):
    if n % 317 == 0:
        total += n
        
print('317の倍数の合計 =', total)

print('処理時間:{}'.format(time.time() - start))

start = time.time()

total = 0
for n in range(317, 1000000001, 317):
    total += n
    
print('317の倍数の合計 =', total)

print('処理時間:{}'.format(time.time() - start))

    