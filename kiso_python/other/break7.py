# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:06:36 2017

@author: tomok
"""

members = ["山田", "横山", "田中", "鈴木", "山本"]

while True:
    member = input("ユーザ名を入力しください: ")
    if member in members:
        print("ようこそ！")
        break
    else:
        print("ユーザ名が正しくありません")