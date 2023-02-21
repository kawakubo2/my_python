# -*- coding: utf-8 -*-

lst = [num ** 2 for num in range(0, 21, 2)]
print(lst)

lst2 = []
for num in range(0, 21, 2):
    lst2.append(num ** 2)
    
print(lst2)