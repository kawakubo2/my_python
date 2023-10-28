"""
(上底 + 下底) * 高さ / 2 --- 台形の面積
(upperbase + lowerbase) * height / 2
"""
# float関数は文字列を小数点に変換する
upperbase = float(input("上底: "))
lowerbase = float(input("下底: "))
height    = float(input("高さ: "))

print("台形の面積: " + str((upperbase + lowerbase) * height / 2))

