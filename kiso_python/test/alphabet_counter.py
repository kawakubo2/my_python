# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:19:56 2020

@author: tomok
"""

import time

start = time.time()
counter = {}

with open('The_Return_of_the_Native_pg122.txt', 'r', encoding='utf_8') as f:
    for line in f:
        for c in line:
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1

for c, num in sorted(counter.items()):
    print('{}: {:5d}'.format(c, num))

end = time.time()
print('処理時間:{}ms'.format(end - start))