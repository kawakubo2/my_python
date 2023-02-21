# -*- coding: utf-8 -*-

import math

radius = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for r in radius:
    print("{:.2f}".format(math.pow(r, 2)*math.pi))
    

tanpen = [(3, 4), (6, 8), (11, 8)]

for t1, t2 in tanpen:
    print(math.hypot(t1, t2))
    print(math.sqrt(math.pow(t1, 2) + math.pow(t2, 2)))