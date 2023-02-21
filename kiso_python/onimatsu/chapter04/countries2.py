# -*- coding: utf-8 -*-

countries = ['イギリス', 'フランス', 'イタリア', 'スペイン', 'ドイツ']

answer = [
    "イギリス","フランス","イタリア","イタリア","フランス",
    "フランス","スペイン","イギリス","フランス","イタリア",
    "イタリア","スペイン","フランス","フランス","スペイン",
    "イタリア","フランス","イタリア","ドイツ","スペイン",
    "イタリア","イタリア","フランス","ドイツ","イタリア",
    "イギリス","フランス","イギリス","イタリア","スペイン",
    "スペイン","イタリア","イギリス","スペイン","イタリア",
    "ドイツ","イギリス","イタリア","スペイン","イタリア"
]

results = {c:0 for c in countries}

for country in answer:
    # results[country] = results[country] + 1 if country in results else 1
   results[country] += 1

        
for country, num in results.items():
    print("{}: {}".format(country, num))