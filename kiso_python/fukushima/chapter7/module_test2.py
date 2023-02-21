# -*- coding: utf-8 -*-

from customer7 import Customer
from customer_m1 import Customer as Cus

taro = Customer(101, "斎藤太郎", 180)
hanako = Customer(102, "山田花子", 165)

jiro = Cus(103, "田中一郎", 172)

print("{} 標準体重:{:.2f}kg".format(taro.name, taro.std_weight()))
print("{} 標準体重:{:.2f}kg".format(hanako.name, hanako.std_weight()))