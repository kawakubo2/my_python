import os


with open(os.path.dirname(__file__) + '/foods.txt', 'r', encoding='utf_8') as f:
    # for food in f:
    #     foods.append(food.rstrip('\n'))
    foods = [food.rstrip('\n') for food in f]
        
print(foods)