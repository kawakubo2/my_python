import math

def menseki(hankai):
    return hankei ** 2 * math.pi

hankei = 10
print(f"半径: {hankei}-> 面積: {menseki(hankei):.3f}")