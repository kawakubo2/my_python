# -*- coding: utf-8 -*-

import random
omikuji = random.randint(1,10)

if omikuji == 1:
    print("大吉")
elif omikuji ==2:
    print("中吉")
elif omikuji <= 4:
    print("小吉")
else:
    print("凶")
