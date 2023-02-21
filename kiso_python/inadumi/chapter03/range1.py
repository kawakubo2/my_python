# -*- coding: utf-8 -*-

print('引数が1個の場合--->開始は0から、引数が終了')
for n in range(10):
    print(n)
    
print('引数が2つの場合--->第1引数が開始、第2引数が終了')
for n in range(10, 21):
    print(n)
    
print('引数が3つの場合--->第1引数が開始、第2引数が終了、第3引数がステップ')
# 0から30までに存在する偶数だけ
for n in range(0, 31, 2):
    print(n)
    
for n in range(10, -1, -1):
    print(n)
    
for n in range(-8, 9):
    print('*' * (n ** 2))
