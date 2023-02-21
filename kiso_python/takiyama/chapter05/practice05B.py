import math

menseki = lambda hankei: hankei * hankei * math.pi

hankei = 10
print(f"半径: {hankei} -> 面積: {menseki(hankei):.3f}")