# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:46:25 2017

@author: tomok
"""

from customer import Customer

taro = Customer(101, "斎藤太郎", 180)
print("{}: {} {}".format(taro.number, taro.name, taro.height))

taro.height = 175
print("{}: {} {}".format(taro.number, taro.name, taro.height))

print("{}の標準体重は{:.2f}kg".format(taro.name, taro.std_weight()))