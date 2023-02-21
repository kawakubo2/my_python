# -*- coding: utf-8 -*-

def gen_list(lst):
    for s in lst:
        yield s.capitalize()

lang = ['python', 'c', 'java', 'basic', 'swift']

for s in gen_list(lang):
    print(s)