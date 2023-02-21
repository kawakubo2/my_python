# -*- coding: utf-8 -*-
import time

start = time.time()

sum = 0
for n in range(317, 1000000001, 317):
    sum += n


end = time.time();
print("処理時間:{:12.6f}秒".format(end - start))
print("合計:{}".format(sum))
