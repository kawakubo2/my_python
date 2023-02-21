name = '山田太郎'
age = 30

print(name + "さんの年齢は" + str(age) + "歳です")
print("%sさんの年齢は%d歳です" % (name, age))
print("{}さんの年齢は{}歳です".format(name, age))
print(f"{name}さんの年齢は{age}歳です")

heisei = 18
print("平成{}年は西暦{}年です。".format(heisei, heisei+1988))
print(f"平成{heisei}年は西暦{heisei + 1988}年です。")

name1 = "山田"
name2 = "鈴木"

print("{1}さん！{0}です。...{1}さんですよね？".format(name1, name2))

body = """
{0}様
{1}年{2}月の新刊情報をお送りします。
・・・・・・・・・・・・・・・・・・
{0}様にはクーポンが発行されていますので
ご利用ください。
"""

year = 2021
month = 5
names = ["山田", "横山", "田中", "鈴木"]

for name in names:
    print(body.format(name, year, month))

upperbase = 1355.1389138
lowerbase = 2314.8971084
height    = 7183.1980581

print("上底が{0:,.1f}cm、下底が{1:,.1f}cm、高さが{2:,.1f}cmの台形の面積は{3:,.1f}平方cmです。".format(
    upperbase, lowerbase, height, ((upperbase + lowerbase) * height) / 2))
