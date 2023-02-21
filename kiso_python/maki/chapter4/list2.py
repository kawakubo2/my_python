# -*- coding: utf-8 -*-

weekdays = ['日', '月', '火', '水', '木', '金', '土']

print(weekdays[:3])
print(weekdays[3:])

weekdays2 = weekdays[1:] + weekdays[0:1]
print(weekdays2)

print(weekdays[::-1])

str_nums = " 1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 "
str_ary = str_nums.split(',')
total = 0
for s in str_ary:
    total += int(s)
    
print('合計:', total)

cities = '　　東京,     大阪  , 名古屋   , 京都　,   青森  '
city_ary = cities.split(',')
for city in city_ary:
    print(city.strip())