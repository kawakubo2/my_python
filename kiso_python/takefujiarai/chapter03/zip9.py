# -*- coding: utf-8 -*-

upper_bases = [231.24, 4.231, 45.18, 3.98, 5.33]
lower_bases = [31.82, 2.72, 113.58, 5.89, 4.38]
heights     = [55.23, 3.87, 444.331, 4.978, 2.69]

str = "上底が{:6.1f}cm、下底が{:6.1f}cm、高さが{:6.1f}cm\
の台形の面積は{:8.1f}平方cmです"
for u, l, h in zip(upper_bases, lower_bases, heights):
    print(str.format(u, l, h, (u + l) + h / 2))