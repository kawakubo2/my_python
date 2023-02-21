# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
    print('引数を指定してください')
    sys.exit(0)
    
sum = 0
for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])
    
print('平均: {:.3f}'.format(sum / (len(sys.argv) - 1)))