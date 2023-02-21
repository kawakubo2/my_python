import math

def calc_charge(unit_price, litter, member = False, discount = 0):
    if member:
        unit_price -= discount
    return math.floor(unit_price * litter)

up = 162
l = 25.7
# m = True
# d = 3

print(f"{calc_charge(up, l)}円")

print(2021, 10, 14, end='', sep='/')
