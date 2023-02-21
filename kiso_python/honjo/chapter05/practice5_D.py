# -*- coding: utf-8 -*-

def gen_list(lst):
    for s in lst:
        yield s.upper()
        #yield s.capitalize()
        
langs = ['ｐｙｔｈｏｎ', 'c', 'java', 'basic', 'swift']

gen = gen_list(langs)

for s in gen:
    print(s)
    
str1 = 'pro linux administratio';
print(str1.title())

str2 = 'p y t h o n';
print(str2.title().replace(' ', ''))