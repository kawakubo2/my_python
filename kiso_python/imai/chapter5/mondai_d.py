# -*- coding: utf-8 -*-

def gen_list(lst):
    for s in lst:
        yield s.upper()


lst = ['python', 'c', 'java', 'basic', 'swift']

for n in gen_list(lst):
    print(n)
    
    
    
for n in (c.upper() for c in lst):
    print(n)