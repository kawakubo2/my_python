# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:51:00 2017

@author: tomok
"""
print('終了のみ指定(終了は含まない)')
for counter in range(10):
    print(counter)

print('開始と終了を指定(終了は含まない)')
for counter in range(10, 20):
    print(counter)

print('第3引数はステップ数を表す')
for counter in range(3, 31, 3):
    print(counter)

numbers = [1, 2, 4, 8, 16]
for i in range(len(numbers)):
    print(numbers[i])
