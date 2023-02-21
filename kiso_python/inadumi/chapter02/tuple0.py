# -*- coding: utf-8 -*-
from myutils import desc

desc(89, 'タプルを生成')
height = 180, 165, 159, 171, 155
desc(89, 'インデックスによるアクセス')
print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])

x = 8
y = 5
print('x={}, y={}'.format(x, y))
y, x = x, y
print('x={}, y={}'.format(x, y))

print('タプルからリストを生成')
height_list = list(height)

print(height_list)
height_list[0] = 183
print(height_list)

book_title = 'learning python for machine learning'
print(book_title.title())

n = 'abc'

if n.isdecimal():
    num = int(n)
    print('num={}'.format(num))
    print('num+10={}'.format(num + 10))
else:
    print('{}は整数に変換できません'.format(n))
    
print('nのid番号は{}'.format(id(n)))

print(id(x))
z = 5
print(id(z))

m = 'abc'
print(id(n))
print(id(m))

print(id(desc))

