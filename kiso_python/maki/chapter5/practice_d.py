# -*- coding: utf-8 -*-

def gen_list(lst):
    for s in lst:
        yield s.capitalize()
        
lst = ['python', 'c', 'java', 'basic', 'swift']

for s in gen_list(lst):
    print(s)