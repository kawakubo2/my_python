# -*- coding: utf-8 -*-

def test1(num):
    print('num: {}'.format(id(num)))
    num += 10
    print('num: {}'.format(id(num)))
    
n = 3
print('n : {}'.format(id(n)))
test1(n)
print(n)
print('n : {}'.format(id(n)))
