dollars = [1, 5, 9.5, 100]

rate = 101

yens = [dollar * rate for dollar in dollars]

print(yens)

members = [(78, 180), (58, 160), (55, 158), (85, 180), (44, 152)]

bmis = [w / (h/100) ** 2 for w, h in members]

print(bmis)

orders = [(500, 6), (400, 8), (300, 8), (700, 4), (350, 10)]

over_3000_orders = [(unit_price, amount) for unit_price, amount in orders if unit_price * amount >= 3000]

print(over_3000_orders)
