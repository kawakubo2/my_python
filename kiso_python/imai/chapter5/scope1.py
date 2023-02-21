# -*- coding: utf-8 -*-

value1 = 1

def scope_test1():
    print('内部:',value1)
    
scope_test1()
print('外部:', value1)

value2 = 1

def scope_test2():
    value2 = 100 # 代入した時点でローカル変数となる
    print('内部:', value2)
    
scope_test2()
print('外部:', value2)

value3 = 1

def scope_test3():
    global value3
    value3 = 100
    print('内部:', value3)
    
scope_test3()
print('外部:', value3)