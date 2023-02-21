# -*- coding: utf-8 -*-

import random

countries = {'イタリア': 13, 'イギリス': 10, 'ドイツ': 8, 'スペイン': 7, 'フランス': 4}

list1 = []

for country, cnt in countries.items():
    list1 += [country + '\n'] * cnt
    
random.shuffle(list1)

with open('countries.txt', 'w', encoding='utf_8') as f:
    f.writelines(list1)