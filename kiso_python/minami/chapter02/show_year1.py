"""
このプログラムはネットワーク帯域が狭い時に動的に
アルゴリズムを変換するためのもの

作成者: 山田太郎
作成日: 2022/11/23
"""
print("西暦" + str(2021) + "年は", end="")
print("令和" + str(2021 - 2018) + "年です")

print("西暦",2021,"年", sep="")
print(2022,11,23, sep="-")

print("""使用法) python3 program1.py ファイル1 ファイル2 ...
例) python3 program1.py test1.txt file12.csv
""")

def add(x, y):
    """
    数値型の引数の和を返す関数
    引数:
        x float: 加算対象の数値1
        y float: 加算対象の数値2

    Returns:
        float : xとyの和
    """
    return x + y

a = 10
b = 20
c = add(a, b)

name = '山田太郎'
name = 123
name = True
name = add
print(name(100, 200))