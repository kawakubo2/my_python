# -*- coding: utf-8 -*-

taro = 170.0
ichiro = 165.5
makoto = 181.5

average = sum([taro, ichiro, makoto]) / 3

print('平均身長: {:.1f}cm'.format(average))

print('平均身長: %.1fcm' % (average))

name = '山田太郎'

age = 43

print('%sさんの年齢は%d歳です' % (name, age))
print('{}さんの年齢は{}歳です'.format(name, age))