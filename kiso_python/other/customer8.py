# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:44:06 2017

@author: tomok
"""

from customer import Customer3

taro = Customer3(101, "斎藤太郎", 180)

name = taro.name
taro.number = 99
number = taro.number
height = taro.height
print("{}: {} {}cm".format(name, number, height))
print("{} {}kg".format(taro.name, taro.std_weight()))
