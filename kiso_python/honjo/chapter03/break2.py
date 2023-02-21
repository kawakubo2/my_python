# -*- coding: utf-8 -*-

secret = "クッキー"

while True:
    word = input('クッキーくれ！ : ')
    if word == secret:
        print("-- ありがとう --")
        break
    else:
        print("-- ちがう！ --")