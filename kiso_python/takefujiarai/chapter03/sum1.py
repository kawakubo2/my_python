# -*- coding: utf-8 -*-
import time

end = int(input('最後の数値を入力してください: '))

starttime = time.time();

sum = 0

for num in range(1, end + 1):
    sum += num
    
endtime = time.time()
print(str(end) + "までの総和:", sum)
print(str(endtime - starttime) + '秒')