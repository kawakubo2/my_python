# -*- coding: utf-8 -*-

def my_gen1(str):
    for c in str.upper():
        yield c
        
for c in my_gen1('HeLlo'):
    print(c)
    
for n in range(10):
    print(n)