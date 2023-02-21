# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 22:02:04 2017

@author: tomok
"""

secret = "foo"

while True:
    word = input("秘密の言葉を入力してください: ")
    if word == secret:
        print("---正解です---")
        break
    else:
        print("---正しくありません---")

