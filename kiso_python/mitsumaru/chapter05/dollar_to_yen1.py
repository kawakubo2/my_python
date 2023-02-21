import math

def dollar_to_yen(dollar, rate):
    return math.floor(dollar * rate)

yen = dollar_to_yen(100, 105)
print("為替レート: 105")
print(f"100ドルは{yen}円")

r = 100
d = 150
yen = dollar_to_yen(dollar = d, rate = r)
print(f"為替レート: {r}")
print(f"{d}ドルは{yen}円")

yen = dollar_to_yen(rate = 110, dollar = 200)
print(f"為替レート: {110}")
print(f"{200}ドルは{yen}円")

def calc_charge(unit_price, quantity):
    return unit_price * quantity

tanka = 50
suryo = 100

kingaku = calc_charge(tanka, suryo)

print(f"単価が{tanka}円、数量が{suryo}の場合、金額は{kingaku}円となります。")

def calc_change(price, unit_price, quantity):
    if price < unit_price * quantity:
        print(f"{unit_price * quantity - price}円金額が不足しています。")
    elif price > unit_price * quantity:
        print(f"おつりは{price - unit_price * quantity}円となります")
    else:
        print("ちょうどいただきました。")

calc_change(1000, 50, 20)
calc_change(1000, 50, 25)
calc_change(1500, 50, 25)

numbers = [10, 2, 13, 24, -5, 6, 18]

def list_sum(nums):
    total = 0
    for num in nums:
        total += num # total = total + num
    return total

print(f"合計: {list_sum(numbers)}")



