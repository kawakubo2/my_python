# show_year1.py

print('西暦' + str(2021) + '年は', end='')
print('令和' + str(2021-2018) + '年です。')

print('A', 123, True, sep='')

# 可変長引数
print(1, 2, 3, 4, 5, 6)
print("""
こんにちは。
今日の福岡は寒くはなかった。
もうすぐ桜が咲くとテレビは言っている。
"""
)
"""
長いコメント
終わり
"""
def add(x, y):
    """
    この関数は数値型の2つの引数を取り、その和を戻り値として返す。
    x: 数値型
    y: 数値型
    戻り値: 数値型
    """
    return x + y

print(add(100, 200))

help(add)

# C, Java
# 静的型付け言語

# 動的型付け言語
a = 100
a = 'abc'
a = True
a = add
print(a(30, 50))