import os

filepath = os.path.join(os.path.dirname(__file__), 'days.txt')

weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

with open(filepath, "w", encoding="utf_8") as f:
    f.writelines([w + "\n" for w in weekdays])