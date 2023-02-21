# -*- coding: utf-8 -*-

names = ['山田', '井上', '太田', '田中', '山田']

name = '山田'
while name in names:
    names.remove(name)

print(names)

names = ['山田', '井上', '太田', '田中', '山田']

name = '山田'

print('{}さんは{}人います'.format(name, names.count(name)))

for n in names:
    if n == name:
        names.remove(name)
        
print(names)

lang1 = ['Python', 'PHP']
lang2 = ['Java', 'JavaScript']

lang3 = []
lang3.extend(lang1)
lang3.extend(lang2)
print(lang3)

names = ['山田', '井上', '太田', '田中', '山田']
del names[1:4]
print(names)

weekdays = ['日', '月', '火', '水', '木', '金', '土']
weekdays.reverse()
print(weekdays)

weekdays = ['日', '月', '火', '水', '木', '金', '土']
weekdays2 = weekdays[::-1]
print(weekdays2)
print(weekdays)

nums = [-1, 9, 4, 10]
print('最大値:{}'.format(max(nums)))
print('最小値:{}'.format(min(nums)))
print('合計:{}'.format(sum(nums)))
