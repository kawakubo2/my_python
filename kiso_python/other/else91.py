# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:54:46 2017

@author: tomok
"""

words = ['旅行', '桜', 'テレビ', '岸辺', 'ラジオ']

for word in words:
    if word == '終了':
        print('ループを中断しました')
        break
    print(word)
else:
    print('ループが完了しました')