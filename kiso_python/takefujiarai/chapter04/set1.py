# -*- coding: utf-8 -*-

lst = [10, 1, 3, 3, 10, 5, 10, 10, 1]

st = set(lst)

print(st)

colors = {'red', 'green', 'blue'}
colors.add('orange')
print(colors)

colors.add('red')
print(colors)

try:
    colors.remove('pink')
    print(colors)
except KeyError:
    print('pinkは存在しません。')
    
if 'pink' in colors:
    colors.remove('pink')
colors.clear()
print(colors)