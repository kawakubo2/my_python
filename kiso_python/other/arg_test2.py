# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:44:32 2017

@author: tomok
"""

def test1(num):
    print("num : {}".format(id(num)))
    print(num ** 2)
    print("num : {}".format(id(num)))
    
n = 3
test1(n)
print(n)
print(id(n))
    