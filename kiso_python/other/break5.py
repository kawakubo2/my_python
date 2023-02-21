# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:49:30 2017

@author: tomok
"""

name = input("名前を入力してください: ")

members = ["山田", "横山", "田中", "鈴木", "山本"]


for member in members:
    if member == name:
        print(name + "さんは名簿に存在します")
        break
else:
    print(name + "さんは名簿に存在しません")
