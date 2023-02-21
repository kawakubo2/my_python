import os

foods = []

# ファイル件数が多く場合の方法
with open(os.path.dirname(__file__) + "/foods.txt", "r", encoding="utf_8") as f:
    for food in f:
        foods.append(food.rstrip("\n"))

print(foods)

# ファイル件数が少ない場合、以下のようにしてもできる
with open(os.path.dirname(__file__) + "/foods.txt", "r", encoding="utf_8") as f:
    foods2 = [food.rstrip("\n") for food in f.readlines()]

print(foods2)