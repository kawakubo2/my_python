# -*- coding: utf-8 -*-

names = ["山田", "井上", "太田", "田中", "山田", "加藤", "山田"]

name = "山田"

while name in names:
    names.remove(name)
    
for n in names:
    print(n + " ", end="")
print("")

names = ["山田", "井上", "太田", "田中", "山田", "加藤", "山田"]

del names[1]

for n in names:
    print(n + " ", end="")
print("")

names = ["山田", "井上", "太田", "田中", "山田", "加藤", "山田"]

del names[1:4]

for n in names:
    print(n + " ", end="")
print("")

weekdays = ["日", "月", "火", "水", "木", "金", "土"]

weekdays.reverse();

print(weekdays)

weekdays2 = weekdays[::-1]

print(weekdays2)

numbers = [3, 52, 31, -10, 8, 7, 123, 45]
my_max = numbers[0]
my_min = numbers[0]
my_sum = 0

for n in numbers:
    if my_max < n:
        my_max = n
    if my_min > n:
        my_min = n
    my_sum += n

print("最大:{},最小:{},合計:{}".format(my_max, my_min, my_sum))

print("最大:{},最小:{},合計:{}".format(max(numbers), min(numbers), sum(numbers)))


