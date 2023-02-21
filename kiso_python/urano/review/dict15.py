

fruits = {'バナナ': 10, 'ミカン': 5, 'イチゴ': 20, 'パイナップル': 2}

while True:
    fruit_name = input('商品名(終了時はq): ')
    if fruit_name == 'q':
        break
    if fruit_name not in fruits:
        print(f"{fruit_name}は売っていません。")
        continue
    quantity = int(input('数量: '))
    if quantity > fruits[fruit_name]:
        print(f"{fruit_name}は{fruits[fruit_name]}しかありません。")
        