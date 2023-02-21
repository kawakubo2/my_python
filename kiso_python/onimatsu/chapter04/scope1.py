# -*- coding: utf-8 -*-
value1 = 1
value3 = 3
def scope_test1():
    value2 = 2
    value3 = 30
    print(value1)
    print(value2)
    print(value3)
    
scope_test1()
print(value3)

def score(name, *nums):
    print('---{}さんの釣果---'.format(name))
    print(nums)
    
score('山田太郎', 30, 50, 70)
score('田中一郎')

def average(*nums):
    return sum(nums) / len(nums)

print(average(1, 2, 3, 4))