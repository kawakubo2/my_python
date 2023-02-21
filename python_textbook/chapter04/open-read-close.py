# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:19:08 2017

@author: tomok
"""

# テキストファイルを開く
a_file = open("mt7_7.txt", encoding="utf-8")

# テキストを読む
s = a_file.read()

# ファイルを閉じる
a_file.close()

# 結果を表示する
print(s)
