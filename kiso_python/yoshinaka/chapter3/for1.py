lst = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']

iter1 = iter(lst)

while True:
    try:
        print(next(iter1))
    except StopIteration:
        break

# シンタックスシュガー(糖衣構文)
for w in lst:
    print(w)
