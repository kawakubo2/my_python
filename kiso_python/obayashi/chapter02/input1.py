"""
input関数でコンソールからデータを取得し
print関数でコンソールに表示する
"""

name = input('名前: ')
height = float(input('身長(cm): '))
weight = float(input('体重(kg): '))

bmi = weight / (height / 100) ** 2

# print関数の使い方の例
print(name, 'さんのBMI値は', bmi, end="")
print("{}さんのBMI値:{:.2f}".format(name, bmi))
print('A', 123, True)
print('ABC', 123.45, True, sep='/')

def add(x, y):
    """
    2つの数値型の引数の和を求め返す
    x: 数値型
    y: 数値型
    戻り値: xとyの和
    """
    if type(x) != float or type(y) != float: 
        raise ValueError("数値でない")
    return x + y

try:
    print(add(12.34, 34.56))
    print(add(12.34, '123'))
except ValueError as e:
    print(e)

def 引き算(x, y):
    return x - y

print(引き算(100, 40))

price = 10000
price = 'abc'
price = True

print(type(price))