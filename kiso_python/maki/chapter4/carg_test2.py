# -*- coding: utf-8 -*-

import sys

sum = 0
for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])
    
print('総和: {}'.format(sum))