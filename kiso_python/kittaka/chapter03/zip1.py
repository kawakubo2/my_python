weekday1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
weekday2 = ["日", "月", "火", "水", "木", "金", "土"]

for en, ja in zip(weekday1, weekday2):
    print(f"{en}: {ja}")

weekday_dict = {}
for en, ja in zip(weekday1, weekday2):
    weekday_dict[en] = ja

print(weekday_dict)