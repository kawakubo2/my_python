print("123456789"[2:6])
s = "123456789"
print(s[0:3]) # s[開始:終了] ・・・開始は含むが終了は含まない
print(s[3:6])
print(s[6:9])

import random

for i in range(30):
    print(random.randrange(5))