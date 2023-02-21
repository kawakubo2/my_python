# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:21:40 2017

@author: tomok
"""
from customer import Customer2

taro = Customer2(101, "斎藤太郎", 180)

print("{} 標準体重:{:.2f}kg".format(taro.get_name(), taro.std_weight()))
