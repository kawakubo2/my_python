bases = [5, 2, 4, 3, 1]
heights = [1, 3, 4, 3, 2]

for base, height in zip(bases, heights):
    print(f"底辺が{base}、高さが{height}の三角形の面積は{base * height / 2}")

vegetables1 = ["かぼちゃ", "じゃがいも", "きゅうり", "にんじん"]
vegetables2 = ["pumpkin", "potato", "cucumber", "carrot"]

for ja, en in zip(vegetables1, vegetables2):
    print(f"{ja}は英語で{en}")