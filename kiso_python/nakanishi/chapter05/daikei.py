def menseki(joutei, katei, takasa):
    return (joutei + katei) * takasa / 2

upperbase = float(input("上底: "))
lowerbase = float(input("下底: "))
height    = float(input("高さ: "))

area = menseki(upperbase, lowerbase, height)
print(f"上底が{upperbase}、下底が{lowerbase}、高さが{height}の台形の面積は{area}")