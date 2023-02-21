# -*- coding: utf-8 -*-

from mystats import MyStats

stats = MyStats([66, 57, 62, 55, 64, 62, 50, 66, 61, 57])

print("平均:{:.1f}".format(stats.mean()))
print("分散:{:.1f}".format(stats.variance()))
print("標準偏差:{:.1f}".format(stats.std()))

print("相関係数:{:.3f}".format(stats.coef([38, 28, 38, 20, 32, 31, 20, 36, 30, 28])))
print("相関係数:{:.3f}".format(stats.coef([58, 100, 72, 48, 18, 79, 28, 8, 92, 10])))

