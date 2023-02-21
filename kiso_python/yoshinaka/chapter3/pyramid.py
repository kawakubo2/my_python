import sys

dansu = int(input('ピラミッドの段数を入力してください: '))

if dansu < 1:
    print('1以上の整数を入力してください')
    sys.exit()

for i in range(dansu):
    print(' ' * (dansu - 1 - i), end='')
    print('*' * (i * 2 + 1), end='')
    print(' ' * (dansu - 1 - i))