# -*- coding: utf-8 -*-

print('○○料金を計算します')

gender = int(input('性別を入力してください 1:女性 2:男性: '))
age = int(input('年齢を入力してください: '))

# 入力値のチェック済みを想定

if gender == 1:
    if age <= 20:
        print('2000円です')
    elif age <= 50:
        print('2200円です')
    elif age <= 70:
        print('2400円です')
    else:
        print('2600円です')
else:
    if age <= 20:
        print('2400円です')
    elif age <= 50:
        print('2800円です')
    elif age <= 70:
        print('3200円です')
    else:
        print('3600円です')
