# zip9.py

# 上底 upperbase, 下底 lowerbase, 高さ height
upperbases = [2, 3, 4, 2, 5, 4]
lowerbases = [3, 3, 2, 4, 2, 3]
heights    = [4, 4, 3, 3, 4, 2]

for upperbase, lowerbase, height in zip(upperbases, lowerbases, heights):
    print((upperbase + lowerbase) * height / 2)
