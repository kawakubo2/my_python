# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:51:56 2017

@author: tomok
"""
import sys

if len(sys.argv) != 2:
    sys.exit(0)

print(sys.argv[0])
dansu = int(sys.argv[1])

for n in range(1, dansu + 1):
    print(' ' * (dansu - n), end="")
    print('*' * (n * 2 - 1), end="")
    print(' ' * (dansu - n))
