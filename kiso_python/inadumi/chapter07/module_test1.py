# -*- coding: utf-8 -*-

import customer_m1

cus1 = customer_m1.Customer(101, '斎藤太郎', 180)
cus2 = customer_m1.Customer(102, '横山花子', 160)

print('{} 標準体重:{:.2f}kg'.format(cus1.name, cus1.std_weight()))
print('{} 標準体重:{:.2f}kg'.format(cus2.name, cus2.std_weight()))