list32 = [
    {'unitprice': 100, 'quantity': 3}, # unitprice(単価) * quantity(数量)
    {'unitprice': 150, 'quantity': 5},
    {'unitprice': 800, 'quantity': 4},
    {'unitprice': 200, 'quantity': 9},
    {'unitprice': 500, 'quantity': 1},
]

# 300 750 3200 1800 500
for item in list32:
    print(item['unitprice'] * item['quantity'])