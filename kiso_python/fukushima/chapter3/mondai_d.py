# -*- coding: utf-8 -*-

try:
    age = int(input('年齢を入力してください : '))
    if  age >= 13:
        print('大人料金です')
    elif 0 < age < 13:
        print('子供料金です')
    else:
        print('年齢は正の整数です')
except ValueError:
    print('正しい年齢を入力してください')