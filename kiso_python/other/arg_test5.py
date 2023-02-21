# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:38:46 2017

@author: tomok
"""

def func(arg1, *arg2):
    print(arg1, arg2)
    
func(1, 2, 3, 4)
func("Hello", "Python", 2015, 3, 5)