seasons = { "春": "Spring", "夏": "Summer", "秋": "Autumn", "冬": "Winter" }

print(seasons.keys())
print(seasons.values())

del seasons["夏"]

print(seasons)

if "晩秋" in seasons:
    del seasons["晩秋"] 

print(seasons)

seasons["秋"] = "Fall"

print(seasons)