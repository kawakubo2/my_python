import math

hankei=10
print('半径: {}-> 面積: {:.3f}'.format(hankei, (lambda hankei: hankei ** 2 * math.pi)(hankei)))