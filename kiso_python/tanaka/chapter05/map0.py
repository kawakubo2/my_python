
def to_cm(inch):
    return inch * 2.54
print('--- map関数を使わない場合 ---')
inches = [9, 5.5, 6, 4, 5, 6.5, 10]
for inch in inches:
    print(to_cm(inch))
print('--- map関数を使う場合 ---')
for cm in map(to_cm, inches):
    print(cm)

def square(x):
    return x * x

for s in map(square, [1, 2, 3, 4]):
    print(s)

import math
def calc_tax(price):
    return math.floor(price * 1.1) 

prices = [1000, 500, 800, 2000]

prices2 = []
for price_with_tax in map(calc_tax, prices):
    prices2.append(price_with_tax)
    
print(prices2)

prices3 = [math.floor(price * 1.1) for price in prices]
print(prices3)

numbers2 = [1, 2, 3, 4]

import math
def circle_area(r):
    return r * r * math.pi

for area in map(math.sqrt, numbers2):
    print(area)