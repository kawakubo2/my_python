# -*- coding: utf-8 -*-

lst1 = ["fly", "good", "ABC", "Bad", "Woo", "Foo", "and"]

lst2 = sorted(lst1, key=str.upper, reverse=True)

print('lst2')
print(lst2)

print('lst1')
print(lst1)

lst1.sort(key=str.upper, reverse=True)
print('lst1')
print(lst1)
