import math

def consumption_tax(price):
    return math.floor(price * 0.1)

p = 2500
tax = consumption_tax(p)
print(f"{p}円の商品の消費税は{tax}円です。")