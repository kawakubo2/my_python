# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:42:57 2017

@author: tomok
"""

import sys

sum = 0

if len(sys.argv) == 1:
    print("使用方法: python practice4_b_2.py 数値1 数値2 ・・・")
    print("例) python practice4_b_2.py 5 4 2 3")
    sys.exit(0)

for i in range(1, len(sys.argv)):
    sum += float(sys.argv[i])

print("平均: {:.3f}".format(sum / (len(sys.argv) - 1)))
