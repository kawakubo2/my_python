# -*- coding: utf-8 -*-

result = {}

with open('answer.txt', 'r', encoding='utf_8') as f:
    for line in f:
        line = line.rstrip('\n')
        if line in result:
            result[line] += 1
        else:
            result[line] = 1
            
for country, num in sorted(result.items(), key=lambda item: item[1], reverse=True):
    print('{}: {}'.format(country, num))