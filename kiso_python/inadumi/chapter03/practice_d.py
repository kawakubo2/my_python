# -*- coding: utf-8 -*-

try:
    age = int(input('年齢を入力してください : '))
    if age <= 0:
        print('年齢は正の整数です')
    elif age < 13:
        print('子供料金です')
    else:
        print('大人料金です')
except ValueError:
    print('正しい年齢を入力してください')