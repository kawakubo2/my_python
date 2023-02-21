# -*- coding: utf-8 -*-

import sys

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
    
print('総和:{}'.format(total))