# -*- coding: utf-8 -*-

def pyramid(n):
    for i in range(n + 1):
        print("{}".format(" "*(n - i)))
        print("{}".format("*"*(i * 2 - 1)))
        
dansu = int(input("ピラミッドの段数を入力してください : "))

pyramid(dansu)