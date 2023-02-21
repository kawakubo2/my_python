# -*- coding: utf-8 -*-

results = {}

with open('answer.txt', 'r', encoding='utf_8') as f:
    for line in f:
        country = line.rstrip('\n')
        if country in results:
            results[country] += 1
        else:
            results[country] = 1

for country in sorted(results.items(), key=lambda c:c[1], reverse=True):
    print("{:4s}: {:3d}".format(country[0], country[1]))