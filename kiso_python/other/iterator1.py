# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:53:26 2017

@author: tomok
"""

try:
    lst = ['春', '夏', '秋', '冬']
    
    itr = iter(lst)
    
    while(True):
        print(next(itr))
except StopIteration as e:
    pass