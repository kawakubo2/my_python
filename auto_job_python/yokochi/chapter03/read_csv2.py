import os, csv, sys

def check_header(header):
    prev_header = ['商品名', '値段', '個数', '小計'] # ファイルから読み込む
    if (len(header) != len(prev_header)):
        return False
    for c_h, p_h in zip(header, prev_header):
        if c_h != p_h:
            return False
    return True


base_dir = os.path.dirname(__file__)
source = os.path.join(base_dir, 'items2.csv')

# header情報を構成ファイル(設定ファイル)に保存

print("商品名                    単価 数量 金額")
first = True
with open(source, encoding='sjis') as f:
    reader = csv.reader(f)
    if first:
        header = next(reader)
        # ファイルへの書き込み
        if not check_header(header):
            print("前回のヘッダーと相違があります。内容を確認の上、再度実行してください。")
            first = False
            sys.exit()
    for line in reader:
        name, unitprice, quantity, subtotal = line
        print(f"{name:20} {unitprice} {quantity} {subtotal}")
