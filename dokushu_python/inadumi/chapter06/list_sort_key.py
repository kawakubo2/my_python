data = ['さくら', 'バラ', 'チューリップ', 'コスモス']
data.sort(key=lambda x: len(x))
print(data)
data = ['さくら', 'バラ', 'チューリップ', 'コスモス']
data2 = sorted(data, key=lambda x: len(x))
print(data2)
print(data)

title = ['部長', '課長', '係長', '主任']
data3 = [
    {'name': '山田太郎', 'position': '主任', 'weight': 72, 'height': 170 },
    {'name': '鈴木次郎', 'position': '部長', 'weight': 72, 'height': 162 },
    {'name': '田中花子', 'position': '課長', 'weight': 72, 'height': 158 },
    {'name': '佐藤恵子', 'position': '係長', 'weight': 72, 'height': 165 },
]

print('---< 役職順でソート')
data3.sort(key=lambda x: title.index(x['position']))
print(data3)

def bmi(weight, height):
    return weight / (height / 100) ** 2

data3.sort(key=lambda x: bmi(x['weight'], x['height']))
for d in data3:
    print(d)
