# -*- coding: utf-8 -*-

a = 10
b = 5

if a > b:
    print('●')

msg = ''

if msg:
    print(msg)
else:
    print('メッセージなし')
    
n = 0

if n:
    print('0以外')
else:
    print('0')
    
lst = []

if lst:
    print('●')
else:
    print('×')
    
b = False

if b:
    print('●')
else:
    print('×')
    
def is_adult(age):
    return age >= 20
    
if is_adult(18):
    print('成人')
else:
    print('未成年')
    
s = '山田太郎'

pos = s.index('山')

if pos >= 0:
    print('山は{}番目に存在する'.format(pos))
else:
    print('山は見つかりませんでした。')