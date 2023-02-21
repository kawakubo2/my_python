vegetables = {'カボチャ': 10, 'ナス': 20, 'ピーマン': 30, 'キュウリ': 15, 'ニンジン': 5}

while True:
    answer = int(input('1.入荷 2.出荷 9.終了: '))
    if answer == 9:
        break
    vegetable_name = input('商品名: ')
    if vegetable_name not in vegetables:
        print(f"{vegetable_name}は扱っておりません。")
        continue
    quantity = int(input('数量: '))
    # 入荷
    if answer == 1:
        vegetables[vegetable_name] += quantity
    # 出荷
    elif answer == 2:
        if quantity > vegetables[vegetable_name]:
            print(f"出荷数量{quantity}が在庫数量{vegetables[vegetable_name]}を上回っています。ご確認ください。")
            continue
        vegetables[vegetable_name] -= quantity    
    else:
        print('1または2を選択してください。')
    print(vegetables)