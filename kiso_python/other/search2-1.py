# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:07:08 2017

@author: tomok
"""

str1 = '木金地火木土'

str2 = input('検索文字列を入力してください: ')

index = str1.find(str2)

if index != -1:
    print('"' + str2 + '"が見つかりました')
    print('インデクス:', index)
else:
    print('"' + str2 + '"が見つかりませんでした')
