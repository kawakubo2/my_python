# -*- coding: utf-8 -*-

lst = ['日','月','火','水','木','金','土']

for day in lst: # シンタックス・シュガー(糖衣構文)
    print(day + '曜日')
    
itr = iter(lst)

try:
    while(True):
        day = next(itr)
        print(day)
except:
    pass
    
    