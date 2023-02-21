# 疑似キュー構造(先入れ先出し(FIFO))

queue = []

while True:
    menu = int(input('1.受付 2.診察 9.終了: '))
    if menu == 9:
        break
    if menu == 1:
        name = input('名前: ')
        queue.append(name)
        print(queue)
    elif menu == 2:
        if len(queue) != 0:
            name = queue.pop(0)
            print(f"{name}さん、診察室へどうぞ。")
            print(queue)
        else:
            print('待合室には誰もいません。')
    else:
        print("1または2を入力してください。")