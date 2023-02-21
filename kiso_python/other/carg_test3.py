# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:56:35 2017

@author: tomok
"""

import sys

sum = 0
for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])
print("総和: {}".format(sum))