import os

foods = []

file = os.path.join(os.path.dirname(__file__), "foods.txt")
with open(file, "r", encoding="utf_8") as f:
    for food in f:
        foods.append(food.rstrip("\n"))
        
print(foods)