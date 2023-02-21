# -*- coding: utf-8 -*-


def add(n1, n2):
    """
    この関数は2つの数値を受け取り、その和を返す
    n1 数値
    n2 数値
    戻り値 数値
    """
    return n1 + n2

print(add(10, 20))

help(add)

name = "山田"
age = 28

print(name, 'さんの年齢は', age, '歳です', sep='')
print('{}さんの年齢は{}歳です'.format(name, age))

name = "冷蔵庫300L"

print(name + "さんの年齢は" + str(age) + "歳です")

# Java  sweetRoomPrice　<--- キャメルケース記法
# C#    SweetRoomPrice <--- パスカル記法
# Python sweet_room_price <--- アンダースコア記法、スネーク記法

num = 100
num += 10 # num = num + 10
print('num =', num)

