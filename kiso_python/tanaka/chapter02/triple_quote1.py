"""
このプログラムはprint関数の使い方と
コメント書き方の練習用です。
"""


# トリプルクウォートは複数行の文字列を入力できる
desc = """この商品は、
JIS規格に準拠しています。
製品説明をよく読んでご使用
ください"""

print(desc)

def add(x, y):
    """
    この関数は2つの数値を加算して返す関数です。
    x: float
    y: float
    戻り値: float
    """
    return x + y

print(add(10, 30))
help(add)

# 動的型付け言語(JavaScript, PHP, Ruby)
# 静的型付け言語(C, Java, C#)
name = "山田太郎"
print(name)
name = 123
print(name)
name = add
print(name(100, 100))

名前 = '田中一郎'
年齢 = 35
print(名前 + 'さんの年齢は' + str(年齢) + '歳です。')

year2 = year1 = 2021
print('year1=' + str(year1))
print('year2=' + str(year2))

a = b = c = d = e = 1