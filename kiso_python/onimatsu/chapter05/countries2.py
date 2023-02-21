# -*- coding: utf-8 -*-

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

results = {}

for country in answer:
    # results[country] = results[country] + 1 if country in results else 1
    if country in results:
        results[country] += 1
    else:
        results[country] = 1
        
for country in sorted(results.items(), key=lambda c:c[1], reverse=True):
    print("{}: {}".format(country[0], country[1]))
    