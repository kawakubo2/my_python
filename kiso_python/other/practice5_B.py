import math

menseki = lambda radius: radius * radius * math.pi

hankei = 10
print("半径 {}-> 面積 {:.3f}".format(hankei, menseki(hankei)))
