# -*- coding: utf-8 -*-

words = ['旅行', '桜', 'テレビ', '岸辺', 'ラジオ']

flag = True
for word in words:
    if word == '終了':
        print('*ループを中断しました')
        flag = False
        break
    print(word)

if flag:
    print('ループが完了しました')

    
