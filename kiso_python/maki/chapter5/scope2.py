# -*- coding: utf-8 -*-

value2 = 2

def scope_test2():
    value2 = 100
    print('関数内value2=', value2)
    
scope_test2()
print(value2)