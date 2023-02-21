# -*- coding: utf-8 -*-

heisei = int(input('平成の年を入力してください: '))

print("平成{}年は西暦{}年".format(heisei, heisei + 1988))

upper_base = 2.3125
lower_base = 1.42521
height     = 3.4891

print("上底が{:.2f}cm、下底が{:.2f}cm、高さが{:.2f}cmの台形の面積は{:.2f}平方cmです"
      .format(upper_base, lower_base, height, (upper_base + lower_base) * height / 2))

print("{1}さん、私は{0}です。...あれ？{1}さんですよね".format("山田", "田中"))
