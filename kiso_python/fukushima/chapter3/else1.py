# -*- coding: utf-8 -*-

words = ['旅行', '桜', 'テレビ', '岸辺', 'ラジオ']

for word in words:
    if word == 'NG':
        print('ループを中断しました')
        break
else:
    print('ループが完了しました')