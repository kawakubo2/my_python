# -*- coding: utf-8 -*-

while True:
    try:
        age = int(input('年齢を入力してください: '))
        if age <= 0:
            print('正の整数を入力してください')
            continue
        elif age < 13:
            print('子供料金です')
            break
        else:
            print('大人料金です')
            break

    except ValueError:
        print('正しい年齢を入力してください')
   
print('ありがとうございました')