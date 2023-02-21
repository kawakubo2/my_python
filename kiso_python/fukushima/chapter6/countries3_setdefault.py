# -*- coding: utf-8 -*-
print('---< setdefaultバージョン >---')
results = {}

with open('countries.txt', 'r', encoding='utf_8') as f:
    for line in f:
        country = line.rstrip('\n')
        results.setdefault(country, 0)
        results[country] += 1
        
for country, num in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print('{}: {}'.format(country, num))