dansu = int(input('ピラミッドの段数: '))

for i in range(1, dansu + 1):
    print("□" * (dansu - i), end="")
    print("■" * (i * 2 - 1), end="")
    print("□" * (dansu - i))