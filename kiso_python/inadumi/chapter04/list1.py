# -*- coding: utf-8 -*-

l1 = ['春', '夏']
l2 = ['秋', '冬']

season = l1 + l2

print(season)
print(l1)
print(l2)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers2 = [1, 2, 4, 8, 16, 32]

numbers3 = numbers1 + numbers2

print(numbers3)

numbers4 = {1, 2, 3, 4, 5, 6, 7, 8}
numbers5 = {1, 2, 4, 8, 16, 32}

numbers6 = numbers4 ^ numbers5
print(numbers6)