# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:12:05 2017

@author: tomoharu
"""

# 単語の出現回数をカウント
text = """
keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 練習問題にはないが、除外したい文字をSetに格納
# 行を「;」で区切っているが、改行コードがOSに依存する
# からだと思われる。Windowsであれば「;」ではなく「\r\n」
delimiters = {";", ",", "."}

for delimiter in delimiters:
    text = text.replace(delimiter, "")

words = text.split()

counter = {}
for word in words:
    w = word.lower()
    if w in counter:
        counter[w] += 1
    else:
        counter[w] = 1

# 練習問題にはないが、出現回数が多い順に表示
for word, count in sorted(counter.items(), key = lambda item: item[1], reverse = True):
    if count >= 3:
        print("{:<15}=>{:>5}".format(word, count))
