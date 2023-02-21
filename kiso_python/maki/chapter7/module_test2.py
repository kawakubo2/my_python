# -*- coding: utf-8 -*-

from customer_m2 import Customer

print("__name__", __name__)
hanako = Customer(101, '山田花子', 165)
print("{} 標準体重: {:.2f}kg".format(hanako.name, hanako.std_weight()))