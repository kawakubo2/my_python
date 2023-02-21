en_seasons = ["Spring", "Summer", "Autumn", "Winter"]
ja_seasons = ["春", "夏", "秋", "冬"]

seasons = {en:ja for en, ja in zip(en_seasons, ja_seasons)}
print(seasons)

strseasons = ["Spring,春", "Summer,夏", "Autumn,秋", "Winter,冬"]

seasons2 = {season.split(",")[0]:season.split(",")[1] for season in strseasons}
print(seasons2)