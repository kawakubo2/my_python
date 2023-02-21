D = 30
for i in range(1, D + 1):
    print(' ' * (D - i), end='')
    print('*' * (i * 2 - 1), end='')
    print(' ' * (D - i))