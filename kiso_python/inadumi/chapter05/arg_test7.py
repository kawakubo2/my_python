# -*- coding: utf-8 -*-

def func(*arg1, arg2):
    print(arg1, arg2)
    
func(1, 2, 3, arg2=4)
func("hello", "Python", 2015, 3, arg2=5)