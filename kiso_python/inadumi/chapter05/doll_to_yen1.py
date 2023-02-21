# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate):
    return doll * rate

yen = doll_to_yen(100, 105)
print('為替レート: {}'.format(105))
print('{}ドルは{}円'.format(100, yen))

r = 100
d = 150

yen = doll_to_yen(d, r)
print('為替レート: {}'.format(r))
print('{}ドルは{}円'.format(d, yen))