#    *
#   ***
#  *****
# *******
#*********

# 空白は(pyramidの段数 - i)
# *はi * 2 - 1

dansu = int(input('ピラミッドの段数を入力してください: '))
for i in range(1, (dansu+1)):
    print(' ' * (dansu - i), end='')
    print('*' * (i * 2 - 1), end='')
    print(' ' * (dansu - i), end='')
    print()