# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:53:43 2017

@author: tomok
"""

str1 = "水金地火木土"

str2 = input("検索文字列を入力してください: ")

if str2 in str1:
    print('"' + str2 + '"が見つかりました')
else:
    print('"' + str2 + '"が見つかりませんでした')
