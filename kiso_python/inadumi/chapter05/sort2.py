# -*- coding: utf-8 -*-

lst1 = ['flyyyyyy', 'good', 'ABC', 'Bad', 'Woooo', 'Foooooooo', 'and']
lst2 = sorted(lst1, key=lambda s: len(s))
print(lst2)
print(lst1)

lst1.sort(key=str.lower)
print(lst1)