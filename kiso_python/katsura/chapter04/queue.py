"""
疑似的なキュー構造
"""

queue = []

while True:
    sw = input("1.受付 2.診察 9.終了: ")
    if sw == '9':
        break
    if sw == '1':
        name = input('名前: ')
        queue.append(name)
        print(queue)
    elif sw == '2':
        if len(queue) == 0:
            print('待合室には誰もいません。')
        continue
        name = queue.pop(0)
        print(f"{name}さん、診察室へどうぞ")
        print(queue)
    else:
        print('1または2を選択してください')