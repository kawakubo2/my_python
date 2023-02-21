# -*- coding: utf-8 -*-

while True:
    try:
        score = int(input('点数を入力してください : '))
    except ValueError:
        print('点数は整数を入力してください。')
        continue
    if 0 <= score <= 100:
        break
    else:
        print('点数は0～100を入力してください。')

print("点数:", score)
        