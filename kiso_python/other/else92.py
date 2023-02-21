# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:01:18 2017

@author: tomok
"""

members = ['山田', '横山', '田中', '鈴木', '山本']

name = input('名前を入力してください： ')

for member in members:
    if member == name:
        print(name + "さんは名簿に存在します")
        break
else:
    print(name + "さんは名簿に存在しません")

