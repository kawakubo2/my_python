# -*- coding: utf-8 -*-

    
students = ['山田', '横山', '田中', '山本', '鈴木']

name = input("名前を入力してください : ")

for s in students:
    if s == name:
        print(name + "さんは名簿にあります。")
        break
else:
    print(name + "さんは名簿にありません。")