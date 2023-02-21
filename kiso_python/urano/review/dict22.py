from re import sub


fruits = [
    {'name': 'バナナ', 'unit_price': 100, 'sales': [ 10, 38, 5, 0, 20, 12, 18 ]},
    {'name': 'リンゴ', 'unit_price': 150, 'sales': [ 5, 5, 10, 7, 8, 2, 20, 22 ]},
    {'name': 'イチゴ', 'unit_price': 300, 'sales': [ 3, 1, 9, 0, 5, 1, 8, 4 ]},
    {'name': 'ブドウ', 'unit_price': 400, 'sales': [ 5, 12, 14, 7, 4, 8, 10 ]},
]

for fruit in fruits:
    subtotal = 0
    for n in fruit['sales']:
        subtotal += n
    print(f"{fruit['name']}\t{fruit['unit_price']}\t{subtotal}\t{fruit['unit_price'] * subtotal}")
    
