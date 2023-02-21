# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate):
    return doll * rate

yen1 = doll_to_yen(doll=100, rate=105)
print('為替レート: {}'.format(105))
print('{}ドルは{}円'.format(100, yen1))

rate2=100
doll2=150
yen2 = doll_to_yen(rate=rate2, doll=doll2)
print('為替レート: {}'.format(rate2))
print('{}ドルは{}円'.format(doll2, yen2))