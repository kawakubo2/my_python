# -*- coding: utf-8 -*-
#sumup1.py

import time

start = time.time()

total = 0

for n in range(317, 1000000001, 317):
    total += n # total = total + n
    
print('合計 =', total)

end = time.time()

print('処理時間: {}'.format(end - start))