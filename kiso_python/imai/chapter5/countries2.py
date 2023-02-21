# -*- coding: utf-8 -*-

countries = ['フランス', 'イギリス', 'イタリア', 'イタリア', 'フランス',
             'イタリア', 'イタリア', 'フランス', 'イギリス', 'イタリア',
             'イギリス', 'イギリス', 'スペイン', 'イタリア', 'イタリア',
             'イタリア', 'スペイン', 'フランス', 'フランス', 'フランス',
             'スペイン', 'フランス', 'ドイツ', 'スペイン', 'イタリア',
             'スペイン', 'イタリア', 'イタリア', 'イタリア', 'スペイン',
             'イタリア', 'イギリス', 'スペイン', 'フランス', 'フランス',
             'イギリス', 'ドイツ', 'ドイツ', 'イタリア', 'スペイン']

results = {}

for country in countries:
    if country in results:
        results[country] += 1
    else:
        results[country] = 1
        
for country, num in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print('{}:{}'.format(country, num))