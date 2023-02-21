seasons = {"春": "Spring", "夏": "Summer", "秋": "Autumn", "冬": "Winter"}

while True:
    season = input("日本語の季節名(終了時はq): ")
    if season == "q":
        break
    if season in seasons:
        print(f"{season}は英語で{seasons[season]}")
    else:
        print(f"{season}は季節名ではありません")