# -*- coding: utf-8 -*-
import random

countries = {'イギリス': 6, 'スペイン': 8, 'イタリア': 14, 'ドイツ': 3, 'フランス': 9}

lst = []

for country, num in countries.items():
    lst += [country] * num
    
random.shuffle(lst)

print(lst)

