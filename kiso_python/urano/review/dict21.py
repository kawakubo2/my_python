import os

def read_fruits():
    fruits = []
    with open(os.path.dirname(__file__) + '/fruits.txt', 'r', encoding='utf_8') as f:
        for line in f:
            name, unit_price, quantity = line.rstrip("\n").split(',')
            fruits.append({'name': name, 'unit_price': int(unit_price), 'quantity': int(quantity)})
    return fruits

fruits = read_fruits()

total = 0
for fruit in fruits:
    total += fruit['unit_price'] * fruit['quantity']
    print(f"{fruit['name']}\t{fruit['unit_price']}\t{fruit['quantity']}\t{fruit['unit_price'] * fruit['quantity']}")
print('----------------------------')
print(f"\t\t\t{total}")
