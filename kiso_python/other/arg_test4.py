# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:14:50 2017

@author: tomok
"""

def test3(lst):
    print("lst: {}".format(id(lst)))
    lst = lst + [3, 4]
    print(lst)
    print("lst: {}".format(id(lst)))

l = [1, 2, 3]
test3(l)
print(l)
print(id(l))