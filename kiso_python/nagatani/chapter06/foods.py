import os

with open(os.path.dirname(__file__) + '/foods.txt', 'r', encoding='utf_8') as f:
    foods = [i.rstrip('\n') for i in f.readlines()]

print(foods)
