# -*- coding: utf-8 -*-

weekdays = ['日', '月', '火', '水', '木', '金', '土']

size = len(weekdays)
for i in range(size):
    if i >= size // 2:
        break
    temp = weekdays[i]
    weekdays[i] = weekdays[size - 1 - i]
    weekdays[size - 1 - i] = temp
    
print(weekdays)

weekdays = ['日', '月', '火', '水', '木', '金', '土']

# 元のリストはそのままで、反転したリストを欲しい時
weekdays2 = weekdays[::-1]

print(weekdays2)

weekdays.reverse()

print(weekdays)