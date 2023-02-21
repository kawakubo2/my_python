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

countries = set()
for a in answer:
    countries.add(a)
    
for country in countries:
    print(country)
    
countries2 = set(answer)
print('--------')
for country in countries2:
    print(country)
