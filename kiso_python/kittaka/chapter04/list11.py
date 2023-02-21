lst = []
lst.append("春")
lst[1:1] = ["夏", "秋", "冬"]
print(lst)
lst.append(["初冬", "晩冬"])
print(lst)

names = ["山田", "井上", "太田", "田中", "山田"]

name = "山田"
while name in names:
    names.remove(name)

print(names)

# リストの内包表記
result = [name for name in names if name != "山田"]
print(result)

if "山田" in names:
    names.remove("山田")

del names[0]

print(names)

weekdays = ["日", "月", "火", "水", "木", "金", "土"]
weekdays.reverse()
print(weekdays)

weekdays = ["日", "月", "火", "水", "木", "金", "土"]
weekdays2 = weekdays[::-1]
print(weekdays2)