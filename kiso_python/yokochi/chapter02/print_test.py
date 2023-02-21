"""
このプログラムは
printの複数の書き方を実験するためのプログラム
コメントの書き方の練習も
"""


print(2021, '年', sep='---------', end='')
print('abc')
year = 2021
print(f"{year}年は令和{year - 2018}年") # 一番新しい書き方
print("{}年は令和{}年".format(year, year - 2018)) # 少し前まで

def add(x, y):
    """
    2つの数値の和を返す関数
    x: 数値
    y: 数値
    戻り値: xとyの和
    """
    return x + y

# print(help(add))
print(add(y = 10, x = 20))

year = input('名前を入力してください')
print(year + 'さん、こんにちは！')

year = lambda x, y: x + y;
print(year(10, 20))

print('Pythonは動的型付け言語')


age = int(input('年齢'))
print(str(age) + '歳ですね')