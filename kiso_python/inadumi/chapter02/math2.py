# -*- coding: utf-8 -*-
import math

print('--- 切上げ関数ceil ---')
num = 1.00001
print(str(num) + 'を切り上げると' + str(math.ceil(num)))

print('--- 切り捨て関数floor ---')
num = 1.99999
print(str(num) + 'を切り捨てると' + str(math.floor(num)))

print('--- 関数exp ---')
exp = 10
print(str(math.e) + 'の' + str(exp) + '乗は' + str(math.exp(exp)))

n = 3
m = 4
print(math.hypot(3, 4))
print(math.sqrt(n ** 2 + m ** 2))

from math import hypot, sqrt, pow

print(hypot(n, m))
print(sqrt(pow(n,2)+pow(m,2)))