# -*- coding: utf-8 -*-

def zero_clear(num):
    num = 0
    
n = 100
zero_clear(n)
print('n={}'.format(n))

def array_zero_clear(narray):
    for i in range(len(narray)):
        narray[i] = 0
        
nums = [1, 2, 3, 4, 5]
print(nums)

array_zero_clear(nums)
print(nums)