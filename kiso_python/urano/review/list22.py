list22 = [
    {"バナナ": 3, "リンゴ": 10, "イチゴ": 20},
    {"バナナ": 10, "リンゴ": 8, "イチゴ": 5},
    {"バナナ": 8, "リンゴ": 20, "イチゴ": 12},
]

# バナナ:   3  10   8   21
# リンゴ:  10   8  20   38
# イチゴ:  20   5  12   37

# 合計だけ出す場合
fruit_dict = {"バナナ": 0, "リンゴ": 0, "イチゴ": 0}
for daily_sales in list22:
    for fruit, quantity in daily_sales.items():
        fruit_dict[fruit] += quantity

for fruit, total in fruit_dict.items():
    print(f"{fruit}: {total}")

# 個数と合計を出す場合
fruit_dict2 = {"バナナ": [], "リンゴ": [], "イチゴ": []}
for daily_sales in list22:
    for fruit, quantity in daily_sales.items():
        fruit_dict2[fruit].append(quantity)
        
for fruit, quantities in fruit_dict2.items():
    fruit_total = 0
    print(fruit, end="")
    for q in quantities:
        fruit_total += q
        print(f"{q:4}", end="")
    print(f"{fruit_total:5}")