# -*- coding: utf-8 -*-

x = 0xF # hexa

print(x + 1)

y = 0o23 # oct

print(y + 5)

z = 0b111111

print(z + 1)

w = 0b1111011

print(w)

s = "He's \"GREAT\" teacher."
print(s)

s = 'He\'s "GREAT" teacher.'
print(s)

s = "私はPython\tを勉強\nしている"
print(s)

num = int("111", 16)
print(num)

num = int("111", 2)
print(num)

print(bin(123))

height = [180, 165, 159, 171, 155]
print(height)
print(type(height))

print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])
# print(height[5])
print('-------------')
height[1] = 182
print(height[1])
print('------< 逆順に取り出す >-------')
print(height[-1])
print(height[-2])
print(height[-3])
print(height[-4])
print(height[-5])
print('------< リストの要素数を調べる >-------')
print(len(height))

print('------< タプル >------')
height = (180, 165, 159, 171, 155)
print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])
# height[1] = 182

print('------< 文字列もシーケンス型 >------')
s = "こんにちは"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

print(id(3))
x = 3
print(id(x))
print(id(10))
print(id(10 + 5))

n1 = 10
n1 += 5


