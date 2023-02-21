# -*- coding: utf-8 -*-

while True:
    score = int(input('点数を入力してください: '))
    if 0 <= score <= 100:
        break
    
print('点数は' + str(score) + '点です。')


