import math

menseki = lambda hankei: hankei * hankei * math.pi

hankei = float(input("半径: "))
print(f"半径: {hankei} -> 面積: {menseki(hankei):.3f}")