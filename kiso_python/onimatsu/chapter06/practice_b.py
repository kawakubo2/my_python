# -*- coding: utf-8 -*-

foods = []

with open('sample2.txt', 'r', encoding='utf_8') as f:
    for food in f:
        foods.append(food.rstrip('\n'))
        
print(foods)