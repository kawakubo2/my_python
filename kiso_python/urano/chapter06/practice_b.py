# practice_b.py

import os

foods = []

with open(os.path.dirname(__file__) + '/foods.txt', 'r', encoding='utf_8') as f:
    for food in f:
        foods.append(food.rstrip('\n'))

print(foods)