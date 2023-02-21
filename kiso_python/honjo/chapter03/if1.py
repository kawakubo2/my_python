# -*- coding: utf-8 -*-

score = int(input('点数を入力してください: '))

if score >= 80:
    print('合格です')
else:
    print('不合格です')

print('合格です' if score >= 80 else '不合格です')

"""
0-11 "おはようございます"
12   "お昼です"
13-18"こんにちは"
19-23"こんばんは"
以外 "範囲外です"

"""