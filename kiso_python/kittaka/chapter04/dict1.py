seasons = {"春": "Spring", "夏": "Summer", "秋": "Autumn", "冬": "Winter"}

for s in seasons.keys():
    print(s)

for s in seasons.values():
    print(s)
    
for ja_s, en_s in seasons.items():
    print(f"{ja_s}: {en_s}")

