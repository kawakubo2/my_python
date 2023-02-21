# -*- coding: utf-8 -*-

str1 = '水金地火木土'

str2 = input('検索文字列を入力してください : ')

try:
    index = str1.index(str2)
    print('"' + str2 + '"が見つかりました')
    print('インデックス:', index)
except ValueError:
    print('"' + str2 + '"が見つかりませんでした')