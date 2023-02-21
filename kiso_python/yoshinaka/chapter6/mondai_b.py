foods = []

with open('foods.txt', 'r', encoding='utf_8') as f:
    for line in f:
        foods.append(line.rstrip('\n'))

print(foods)
