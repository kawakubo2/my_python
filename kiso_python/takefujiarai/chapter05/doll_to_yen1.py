# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate):
    return doll * rate

yen1 = doll_to_yen(100, 105)
print('為替レート: {}'.format(105))
print('{}ドルは{}円'.format(100, yen1))

rate2 = 100
doll2 = 150
print('為替レート: {}'.format(rate2))
print('{}ドルは{}円'.format(doll2, doll_to_yen(doll2, rate2)))

def consumption_tax(price, tax_rate=0.08):
    return price * tax_rate

p = 1000
rate3 = 0.10
print('{}の消費税額は{}です'.format(p, 
      consumption_tax(tax_rate=rate3, price=p)))

p = 1000
print('{}の消費税額は{}です'.format(p, 
      consumption_tax(p)))
