# -*- coding: utf-8 -*-

words = ['旅行', '桜', 'テレビ', '終了', '岸辺', 'ラジオ']

done = True

for word in words:
    if word == "終了":
        print("ループを中断しました")
        done = False
        break
    print(word)

if done:
    print("ループが終了しました")
    
for word in words:
    if word == "終了":
        print("ループを中断しました")
        break
    print(word)
else:
    print("ループが終了しました")
    