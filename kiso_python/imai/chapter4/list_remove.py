# -*- coding: utf-8 -*-

names = ['横山', '山田', '田中', '山田', '鈴木', '山田']

n = '山田'

while n in names:
    names.remove(n)
    
print(names)

names = [n for n in names if n != '山田']
print(names)

names = ['横山', '山田', '田中', '山田', '鈴木', '山田']

try:
    while len(names) > 0:
        pos = names.index('山田')
        del names[pos]
except ValueError:
    pass

print(names)

weekdays = ['日', '月', '火', '水', '木', '金', '土']

weekdays2 = weekdays[::-1]

print(weekdays)
print(weekdays2)

nums = [3, 1, 19, 4, 7, 12, 6, 2]
print('合計:', sum(nums))
print('平均:', sum(nums) / len(nums))
print('最大:', max(nums))
print('最小:', min(nums))
print('件数:', len(nums))