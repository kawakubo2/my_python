# -*- coding: utf-8 -*-



while(True):
    score = int(input('点数を入力してください:'))
    if 0 <= score <= 100:
        break

if score >= 80:
    print('合格です')
else:
    print('不合格です')
