# -*- coding: utf-8 -*-

results = {}

with open("answer.txt", "r", encoding="utf-8") as f:
    for line in f:
        country = line.rstrip("\n")
        if country in results:
            results[country] += 1
        else:
            results[country] = 1
            
for country, cnt in sorted(results.items(), key=lambda c: c[1], reverse=True):
    print("{}: {}".format(country, cnt))