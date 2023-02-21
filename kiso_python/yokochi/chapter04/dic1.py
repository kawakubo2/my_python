# dic1.py

seasons = {"春": "Spring", "夏": "Summer", "秋": "Autumn", "冬": "Winter"}

ja_season = input('季節名: ')
if ja_season in seasons:
    print(seasons[ja_season])
else:
    print(f"{ja_season}は辞書にありません。")