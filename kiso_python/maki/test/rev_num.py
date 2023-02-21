# -*- coding: utf-8 -*-

# 4815
def rev_num(num):
    result = 0
    while(num > 0):
        result = result * 10 + num % 10
        num //= 10
    return result
        
a = 4815
print('{}を逆順にすると{}'.format(a, rev_num(a)))
