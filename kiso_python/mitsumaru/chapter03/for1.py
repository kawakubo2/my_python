lst = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']

for day in lst:
    print(day)

for c in "日月火水木金土":
    print(c + "曜日")

lst2 = [c + "曜日" for c in "日月火水木金土"]
print(lst2)

# シンタックスシュガー(糖衣構文)
for c in "三丸奈々":
    print(c + ":" + str(ord(c)))