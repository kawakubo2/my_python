# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:17:24 2017

@author: tomok
"""

for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + "*" + str(j) + \
        "=" + str(i * j) + ", ", end="")
    print("")
print("")

for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 30:
            break
        print("{}*{}={}, ".format(i, j, i * j), end="")
    print("")
print("")
    