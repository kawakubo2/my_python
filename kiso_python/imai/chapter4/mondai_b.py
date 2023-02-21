# -*- coding: utf-8 -*-

import sys


# python mondai_b.py 2.3 5.25 7.3

if len(sys.argv) < 2:
    sys.exit(-1)

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
    
print('平均: {:.3f}'.format(total / (len(sys.argv) - 1)))