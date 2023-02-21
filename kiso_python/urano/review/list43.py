list43 = [
    "バナナ,150,3", "リンゴ,80,5", "ブドウ,300,2"
]

# フルーツ名,単価,数量
#
# バナナ: 450 リンゴ 400 ブドウ: 600

for fruit in list43:
    name, unit_price, quantity = fruit.split(',')
    print(f"{name}: {int(unit_price)*int(quantity)}")