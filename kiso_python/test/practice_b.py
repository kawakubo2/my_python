# -*- coding: utf-8 -*-

taro = 170.0
ichiro = 165.5
makoto = 181.5

average = (taro + ichiro + makoto) / 3

print("平均身長: " + str(average) + "cm")
print("平均身長: %.1fcm" % (average))
print("平均身長: {:.1f}cm".format(average))

colors = ['赤', '青', '黄', 'オレンジ']

n = 2
if 0 <= n < len(colors):
    print(colors[n])