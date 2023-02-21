# -*- coding: utf-8 -*-

def test1(num):
    num += 10
    print('num=', num)
    
n = 3
test1(n)
print(n)


list1 = [1, 2, 3, -100, 100, 15]

def clear(lst):
    for i in range(len(lst)):
        lst[i] = 0



        
print(list1)
clear(list1)
print(list1)

def clear2(lst):
    for n in lst:
        n = 0
        
list2 = [10, 20, 30, 40, 50]
print(list2)
clear2(list2)
print(list2)

list3 = [1, 2, 3]

def test3(lst):
    lst = lst + [4, 5]
    return lst
    
print(list3)
list4 = test3(list3)
print(list3)
print(list4)