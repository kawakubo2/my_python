# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:00:22 2017

@author: tomok
"""
# 参照の値渡し
def test2(lst):
    print("lst: {}".format(id(lst)))
    for i in range(len(lst)):
        lst[i] = lst[i] * 2
    #  for n in lst:
    #    n *= 2
    print("lst: {}".format(id(lst)))

l = [1, 2, 3]
test2(l)
print(l)
print("l: {}".format(id(l)))