# -*- coding: utf-8 -*-

# 上底
upperbases = [4, 2, 3, 6, 2]
# 下底
lowerbases = [6, 2, 1, 4, 7]
# 高さ
heights    = [3, 6, 5, 4, 8]

for upperbase, lowerbase, height in zip(upperbases, lowerbases, heights):
    print((upperbase + lowerbase) * height / 2)
