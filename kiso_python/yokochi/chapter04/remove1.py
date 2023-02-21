names = ['山田', '井上', '太田', '田中', '山田', '鈴木', '山田']

name = '山田'

while name in names:
    names.remove(name)

print(names)

weekdays = ['日', '月', '火', '水', '木', '金', '土']

weekdays2 = weekdays[-1::-1]
print(weekdays2)
print(weekdays)

weekdays3 = weekdays[::]
if id(weekdays3) == id(weekdays):
    print('同じオブジェクト')
else:
    print('異なるオブジェクト')

weekdays4 = ['ニチ', 'ゲツ', 'カ', 'スイ', 'モク', 'キン', 'ド']
print(max(weekdays4))
print(min(weekdays4))