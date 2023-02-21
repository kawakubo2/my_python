# -*- coding: utf-8 -*-

try:
    score = int(input('点数を入力してください : '))
    if score >= 80:
        print('合格')
    else:
        print('不合格')
    print('処理成功')
except ValueError:
    print('整数値を入力してください')
    
