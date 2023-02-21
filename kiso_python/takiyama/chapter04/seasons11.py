seasons = {"春": "Spring", "夏": "Summer", "秋": "Autumn", "冬": "Winter"}

for key in seasons.keys():
    print(key)
    
for value in seasons.values():
    print(value)
    
for key, value in seasons.items():
    print(f"{key}: {value}")