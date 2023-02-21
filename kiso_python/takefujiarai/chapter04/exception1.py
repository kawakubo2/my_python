# -*- coding: utf-8 -*-
while True:
    try:
        score = int(input('点数を入力してください: '))
        break
    except ValueError:
        print('数値を入力してください')
        
if score >= 80:
    print('合格')
else:
    print('不合格')
