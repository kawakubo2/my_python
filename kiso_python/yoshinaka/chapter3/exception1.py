import sys

while True:
    try:
        score = int(input('点数を入力してください: '))
        break
    except ValueError:
        print('整数を入力してください')

if score >= 80:
    print('合格です。')
else:
    print('不合格です。')