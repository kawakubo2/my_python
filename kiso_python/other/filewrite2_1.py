weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

with open("days.txt", "w", encoding="utf_8") as f:
    f.writelines([c + "\n" for c in weekdays])
