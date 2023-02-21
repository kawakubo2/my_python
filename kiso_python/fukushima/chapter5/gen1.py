# -*- coding: utf-8 -*-

def my_gen1(str):
    for c in str.upper():
        yield c
        
try:
    gen = my_gen1('HeLlo')
    while(True):
        print(next(gen))
except StopIteration:
    pass

for c in my_gen1('abcDeF'):
    print(c)
    