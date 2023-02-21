lst = [num ** 2 for num in range(0, 21, 2)]
print(lst)

total = sum([num ** 2 for num in range(0, 21, 2)])
print(f"合計: {total}")

s = "日月火水木金土"
wod = [w + "曜日" for w in s]
print(wod)