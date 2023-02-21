# -*- coding: utf-8 -*-
import math

radius = [1, 2, 3, 4, 5]

area = [r * r * math.pi  for r in radius]

print(area)

numbers = [5, 6, 7, 5, 4, 9, 6, 3, 6, 5]

avg1 = sum(numbers) / len(numbers)
print(avg1)

var1 = sum([(n - avg1) ** 2 for n in numbers]) / len(numbers)

print("分散:{} 標準偏差:{}".format(var1, var1 ** 0.5))

total = 0
for n in numbers:
    total += (n - avg1) ** 2
print(total / len(numbers))

building_age = [12, 8, 23, 35, 7, 25, 29, 19, 30, 11]
prices = [2400, 3100, 1800, 1200, 3500, 1900, 2000, 2000, 1500, 3500]

age_avg1 = sum(building_age) / len(building_age)
price_avg1 = sum(prices) / len(prices)

print("築年数の平均:{} マンション価格の平均:{}".format(age_avg1, price_avg1))

age_std = (sum([(age - age_avg1) ** 2 for age in building_age])\
           / len(building_age)) ** 0.5
price_std = (sum([(price - price_avg1) ** 2 for price in prices])\
            / len(prices)) ** 0.5
print("築年数の標準偏差:{} マンション価格の標準偏差:{}".format(age_std, price_std))
             
covar1 = sum([(age - age_avg1) * (price - price_avg1)\
              for age, price in zip(building_age, prices)]) / len(prices)
    
print("共分散:{}".format(covar1))
coef1 = covar1 / (age_std * price_std)
print('築年数とマンション価格の相関係数は{}です。'.format(coef1))

