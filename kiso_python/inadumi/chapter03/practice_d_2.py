# -*- coding: utf-8 -*-

while True:
    try:
        age = int(input('年齢を入力してください : '))
        if age <= 0:
            print('年齢は正の整数です')
        elif age < 13:
            print('子供料金です')
        else:
            print('大人料金です')
        
        if age > 0:
            break
    except ValueError:
        print('年齢の形式に誤りがあります')
        age = 0