# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:36:16 2017

@author: tomok
"""

words = ['旅行', '桜', 'テレビ', 'NG', '岸辺', 'ラジオ']

for word in words:
    if word == '終了':
        print('ループが中断しました')
        break
    print(word)
else:
    print('ループが完了しました。')