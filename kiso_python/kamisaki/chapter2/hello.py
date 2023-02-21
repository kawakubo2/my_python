DANSU = int(input('ピラミッドの段数: '))

for i in range(1, DANSU+1):
    print(' ' * (DANSU - i), end='')
    print('*' * (i * 2 - 1), end='')
    print(' ' * (DANSU - i))