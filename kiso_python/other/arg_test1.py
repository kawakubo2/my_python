# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:31:43 2017

@author: tomok
"""

def doll_to_yen(doll, rate=105):
    return doll * rate
    
print(doll_to_yen(100))
print(doll_to_yen(100, 120))


def doll_to_yen2(doll=100, rate=105):
    return doll * rate

print(doll_to_yen2(200, 120))
print(doll_to_yen2(200))
print(doll_to_yen2())