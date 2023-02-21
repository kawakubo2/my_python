e_seasons = ["Spring", "Summer", "Autumn", "Winter"]
j_seasons = ["春", "夏", "秋", "冬"]

seasons_en = { en:ja for en, ja in zip(e_seasons, j_seasons)}
print(seasons_en)

seasons_ja = { ja:en for en, ja in zip(e_seasons, j_seasons)}
print(seasons_ja)