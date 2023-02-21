print('こんにちは、世界！')
print('こんにちは、Python！')

print(4 + 5)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# (5 + 4) * (7 / 4)

print(mul(add(5, 4), div(7, 4)), end='')
print('aaa')

print('a', 'b', 'あ', 123, sep='@')
print()

# ここはコメント
"""
ajgekgj
egaoiga
"""
x = """こんにちは。
今日の福岡は
32度まで上がったようです。
"""
print(x)

def add(x, y):
    """
    2つの数値を受け取り、その和を返す
    x: 数値
    y: 数値
    戻り値: xとyの和
    """
    return x + y

print(help(add))

print(help(print))