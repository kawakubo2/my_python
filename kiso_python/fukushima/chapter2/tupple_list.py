# -*- coding: utf-8 -*-

# tupple_list.py

t1 = ('赤', '黒', '緑')

l1 = list(t1)

l1[0] = '黄色'

print(l1)

t2 = tuple(l1)

print(t2)

weekdays = '日月火水木金土'

list1 = []
for w in weekdays:
    list1.append(w + '曜日')
    
print(list1)