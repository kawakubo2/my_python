lst = ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"]

# 糖衣構文(シンタックス・シュガー)
for day in lst:
    print(day)

itr = iter(lst)

print('--- iterを使った繰り返し構文 ---')
while True:
    try:
        print(next(itr))
    except:
        break