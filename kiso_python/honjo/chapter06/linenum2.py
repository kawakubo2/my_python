# -*- coding: utf-8 -*-

f = open('numbers.csv', 'r', encoding='utf_8')
lines = f.readlines()
for line in lines:
    numbers = line.rstrip('\n').split(',')
    #print(numbers)
    total = 0
    for num in numbers:
        print(num + ',', end='')
        total += int(num)
    print("合計:{}".format(total))
    
f.close()