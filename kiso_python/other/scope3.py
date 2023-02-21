# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:27:21 2017

@author: tomok
"""

value3 = 1 #グローバル変数

def scope_test3():
    value3 = 100 #ローカル変数
    print("内部: ", value3)
    
scope_test3()
print("外部: ", value3)