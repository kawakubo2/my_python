import math
hankei = float(input('半径を入力してください: '))

menseki = math.pi * math.pow(hankei, 2)

# 1
print("半径が" + str(hankei) + "の円の面積 → ", menseki);
# 2
print("半径が%7.2fの円の面積は%7.2f" % (hankei, menseki))
# 3
# print("半径が{1:7.2f}の円の面積は{0:7.2f}".format(menseki, hankei))
print("半径が{:7.2f}の円の面積は{:7.2f}".format(hankei, menseki))
# 4
print(f"半径が{hankei:7.2f}の円の面積は{menseki:7.2f}")


