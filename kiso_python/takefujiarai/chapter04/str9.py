# -*- coding: utf-8 -*-

email = 'tomo.kawakubo@gmail.com'

pos = email.find('@')

local = email[:pos]
domain = email[pos+1:]

print('ローカル部:' + local)
print('ドメイン部:' + domain)

upper_base = 5.2345
lower_base = 4.92093
height     = 6.80913
area = (upper_base + lower_base) * height / 2

print('上底が{:.2f}cm、下底が{:.2f}cm。高さが{:.2f}cmの\
台形の面積は{:.2f}平方cmです'.format(upper_base, lower_base\
, height, area))

name1 = '川久保'
name2 = '光武'

print('{1}さん、{0}です。・・・あれ？{1}さんですよね?'.format(name1, name2))

# 整数値  :3d 
# 文字列  :10s