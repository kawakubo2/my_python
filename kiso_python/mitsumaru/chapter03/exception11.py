try:
    numbers = []
    while True:
        s = input('整数(終了はq): ')
        if s == "q":
            break
        numbers.append(int(s))
    while True:
        s = input('リストのインデックス(終了はq):')
        if s == "q":
            break
        print(numbers[int(s)])
except ValueError:
    print('整数を入力してください')
except IndexError:
    print(f"インデックスの範囲は0～{len(numbers)}です。")