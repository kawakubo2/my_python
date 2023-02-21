# -*- coding: utf-8 -*-

import math, sys

if len(sys.argv) != 3:
    print('使用法: python distance1.py x座標 y座標')
    print('例: python distance1.py 4.0 3.0')
    sys.exit()
    
x = float(sys.argv[1])
y = float(sys.argv[2])

print(math.sqrt(x ** 2 + y ** 2))