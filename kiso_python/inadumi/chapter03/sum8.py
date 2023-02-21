# -*- coding: utf-8 -*-
import time

print('1～1億までに存在する317の倍数の合計')

max = 100000000

print('---< 解法1 >---')
start = time.time()
sum = 0
for num in range(1, max + 1):
    if num % 317 == 0:
       sum += num
      
print('合計:' + str(sum))
end = time.time()
print('処理時間:' + str(end - start))

print('---< 解法2 >---')
start = time.time()
sum = 0
for num in range(317, max + 1, 317):
    sum += num

print('合計:' + str(sum))
end = time.time()
print('処理時間:' + str(end - start))