# -*- coding: utf-8 -*-

results = {}

with open('answer.txt', 'r', encoding='utf_8') as f:
    for line in f:
        country = line.rstrip('\n')
        results[country] = results[country] + 1 if country in results else 1
        
for country in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print('{}: {}'.format(country[0], country[1]))