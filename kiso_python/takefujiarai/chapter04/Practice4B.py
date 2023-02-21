# -*- coding: utf-8 -*-

import sys

sum = 0

if len(sys.argv) <= 1:
    print('使用法: python Practice4B.py 数値1 数値2 ...')
    print('例: python Practice4B.py 1.5 5.3 2.4')
    sys.exit(1)

for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])
    
print('平均: {:.3f}'.format(sum / (len(sys.argv) - 1)))