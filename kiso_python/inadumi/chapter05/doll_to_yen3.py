# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate=100):
    return doll * rate

print('*** rateを指定した場合は、デフォルト値は使用されない ***')
doll1 = 100
yen = doll_to_yen(doll1, 105)
print('為替レート: {}'.format(105))
print('{}ドルは{}円'.format(doll1, yen))

print('*** rateを指定しない場合は、デフォルト値が使用される ***')
doll2 = 50
yen = doll_to_yen(doll2)
print('為替レート: {}'.format(100))
print('{}ドルは{}円'.format(doll2, yen))