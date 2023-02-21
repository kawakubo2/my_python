# -*- coding: utf-8 -*-

upper_bases = [2, 3, 1, 5, 4]
lower_bases = [3, 5, 7, 8, 5]
heights     = [4, 7, 6, 2, 3]

for u, l, h in zip(upper_bases, lower_bases, heights):
    print("上底が{}cm、下底が{}cm、高さが{}cmの台形の面積は\
{}平方cmです。".format(u, l, h, (u + l) * h / 2))