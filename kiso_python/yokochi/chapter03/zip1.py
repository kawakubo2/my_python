import sys

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']

if len(weekday1) != len(weekday2):
    print('2つのリストの要素数が等しくありません')
    sys.exit()

for en, ja in zip(weekday1, weekday2):
    print(f"{en}: {ja}")

# 台形の面積
upperbases = [1, 2, 3, 4, 5]
lowerbases = [3, 2, 1, 2, 1]
heights    = [4, 3, 2, 1, 3]

for upper, lower, height in zip(upperbases, lowerbases, heights):
    print((upper + lower) * height / 2)

members = ['山田', '田中', '横山', '山本', '鈴木']

name = '遠藤'

for member in members:
    if member == name:
        print(f"{name}さんは名簿に存在します")
        break
else:
    print(f"{name}さんは名簿に存在しません")

not_exists_flag = True
for member in members:
    if member == name:
        print(f"{name}さんは名簿に存在します")
        not_exists_flag = False 
        break

if not_exists_flag:
    print(f'{name}さんは名簿に存在しません')