# -*- coding: utf-8 -*-

name=58
age=43
age2=age
name=123
print(str(name) + 'さんの年齢は' + str(age) + '歳です')

n = 10
# n = n + 5
# nに5を加算後、その結果をnに代入する
n += 5
print(n)
# n = n - 8
n -= 8
print(n)
# n = n * 2
n *= 2
print(n)
# n = n / 7
n /= 7
print(n)

n %= 3
print(n)

n = 7.5
n %= 1.2
print(n)

名前='山田太郎'
print(名前)

def 階乗(num):
    if num == 0:
        return 1
    else:
        return num * 階乗(num - 1)
    
print(階乗(5))

print(123, 'abc', 5.234, sep='@', end='')
print('Hello')

