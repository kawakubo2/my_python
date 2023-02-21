# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:14:36 2017

@author: tomoharu
"""

# 成績データ辞書型で定義
records = {
        "Tanaka": 72, "Yamada": 65, "Hirata": 100,
        "Akai": 56, "Fukuda": 66, "Sakai": 80
}

sum = 0
for score in records.values():
    sum += score

avg = sum / len(records)
print("合計点: {}".format(sum))
print("平均点: {:.1f}".format(avg))
print("+--------+------+------+")
print("|name    | score|  diff|")
print("+--------|------|------+")
# 成績の低い順にソート
for name, score in sorted(records.items(), key = lambda item: item[1]):
    diff = score - avg
    print("|{0:<7} | {1:>4} | {2:>5.1f}|".format(name, score, diff))
print("+--------+------+------+")
