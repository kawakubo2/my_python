# -*- coding: utf-8 -*-

uriage = [10, 12, 13, 31, 8, 9, 21, 5, 18, 28]

total = 0
for price in uriage:
    total = total + price
    
print('売上は{}万円です。'.format(total))