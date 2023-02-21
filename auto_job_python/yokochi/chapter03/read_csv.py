import os, csv, pprint

base_dir = os.path.dirname(__file__)
source_file = os.path.join(base_dir, 'items.csv')

# csvモジュールを使わない方法
with open(source_file, encoding='sjis') as f:
    text = f.read().strip()
    lines = text.split('\n')
    data = [v.split(',') for v in lines]
    pprint.pprint(data)

import math
def price_with_tax(price):
    return math.floor(float(price) * 1.08)
# csvモジュールを使う方法
with open(source_file, encoding='sjis') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    pprint.pprint(data)
    itemname, unitprice, quantity, subtotal = data[0]
    print(f"{itemname} {unitprice} {quantity} {subtotal} 税込み金額")
    print('----------------------')
    for i in range(1, len(data)):
        print(f"{data[i][0]}   {data[i][1]}   {data[i][2]}   {data[i][3]} {price_with_tax(data[i][3])}円")

