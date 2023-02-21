# -*- coding: utf-8 -*-

def test1(num):
    num += 10
    
n = 3
test1(n)
print(n)

def test2(nums):
    nums[0] += 10
    
list1 = [1, 2, 3, 4, 5]
print('test2関数呼び出し前:', end='')
print(list1)
test2(list1)
print('test2関数呼び出し後:', end='')
print(list1)