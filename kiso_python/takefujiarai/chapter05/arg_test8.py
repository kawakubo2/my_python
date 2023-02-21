# -*- coding: utf-8 -*-

def func(**dic):
    print(dic)
    
func(name='田中一郎', num=1)
func(name='山田太郎', age=59, num=2, point=60)

def add(x, y):
    return x + y

print(add(10, 20))

myadd = lambda a, b: a + b

print(myadd(5, 7))