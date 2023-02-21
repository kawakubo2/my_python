# -*- coding: utf-8 -*-

with open("out.txt", "a", encoding="utf-8") as f:
    while True:
        text = input("文字列を入力してください(終了時はquit): ")
        if text == "quit":
            break
        f.write(text + "\n")