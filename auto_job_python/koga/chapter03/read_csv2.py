import csv, os

with open(os.path.dirname(__file__) + "/items2.csv", "r", encoding="sjis") as f:
    reader = csv.reader(f)
    # ヘッダー行をスキップ
    head = next(reader)
    # 1行ずつ調べる
    total = 0
    for row in reader:
        name,price,cnt,subtotal=row
        print(name,price,cnt,subtotal)
        total += int(subtotal)
    print(f"合計: {total}")