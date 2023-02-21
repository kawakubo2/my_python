# -*- coding: utf-8 -*-

foods = []

with open('foods.txt', 'r', encoding='utf_8') as f:
    for food in f:
        foods.append(food.rstrip('\n'))
        
print(foods)

with open('foods2.txt', 'w', encoding='utf_8') as f:
    for food in [food + '\n' for food in foods]:
        f.write(food)