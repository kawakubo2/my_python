import os

foods = []

with open(os.path.dirname(__file__) + "/foods.txt", "r", encoding="UTF-8") as f:
    for food in f:
        foods.append(food.rstrip("\n"))

print(foods)