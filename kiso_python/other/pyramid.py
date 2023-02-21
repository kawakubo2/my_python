# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:51:56 2017

@author: tomok
"""

dansu = int(input('ピラミッドの段数を入力してください: '))

for n in range(1, dansu + 1):
    print(' ' * (dansu - n), end="")
    print('*' * (n * 2 - 1), end="")
    print(' ' * (dansu - n))
