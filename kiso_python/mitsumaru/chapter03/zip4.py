upperbases = [1.23, 4.28, 3.81, 2.81, 5.08] # 上底のリスト
lowerbases = [0.87, 1.80, 2.28, 3.13, 2.96] # 下底のリスト
heights    = [2.37, 3.56, 4.69, 3.38, 3.09] # 高さのリスト

for upperbase, lowerbase, height in zip(upperbases, lowerbases, heights):
    print("{:.2f}".format((upperbase + lowerbase) * height / 2))