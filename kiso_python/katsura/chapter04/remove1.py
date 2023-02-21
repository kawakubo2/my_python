names = ['山田', '井上', '山田', '太田', '田中', '山田']
name  = '山田'
while name in names:
    names.remove(name)

print(names)

names2 = [name for name in names if name != '山田']
print(names2)

weekdays = ['日', '月', '火', '水', '木', '金', '土']
weekdays.reverse()
print(weekdays)

weekdays = ['日', '月', '火', '水', '木', '金', '土']
weekdays2 = weekdays[::-1]
print(weekdays2)