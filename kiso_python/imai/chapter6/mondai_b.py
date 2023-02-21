foods = []

with open('foods.txt', 'r', encoding='utf_8') as f:
    for food in f:
        foods.append(food.rstrip('\n'))

print(foods)