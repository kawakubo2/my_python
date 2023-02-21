import collections

data = collections.deque()

while True:
    sw = int(input('1.受付 2.診察 9.終了: '))

    if sw == 9:
        break
    if sw == 1:
        name = input('名前:')
        data.append(name)
        print(data)
    elif sw == 2:
        if len(data) > 0:
            name = data.popleft()
            print(name + 'さん、診察室へどうぞ')
        else:
            print('待合室には誰もいません。')
        print(data)
    else:
        print('1または2を指定してください')
    