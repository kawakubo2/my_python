# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate):
    return doll * rate

doll1 = 100
rate1 = 105

yen1 = doll_to_yen(doll1, rate1)
print('為替レート: {}'.format(rate1))
print('{}ドルは{}円'.format(doll1, yen1))

doll2 = 100
rate2 = 150

yen2 = doll_to_yen(doll2, rate2)
print('為替レート: {}'.format(rate2))
print('{}ドルは{}円'.format(doll2, yen2))

doll3 = 100
rate3 = 120

yen3 = doll_to_yen(doll=doll3, rate=rate3)
print('為替レート: {}'.format(rate3))
print('{}ドルは{}円'.format(doll3, yen3))

doll4 = 100
rate4 = 120

yen4 = doll_to_yen(rate=rate4, doll=doll4)
print('為替レート: {}'.format(rate4))
print('{}ドルは{}円'.format(doll4, yen4))

print(100, 200, 300)
print(100, 200, 300, sep=':')

def discount_price(price, rate, currency='JPY'):
    import math
    if currency == 'JPY':
        return '￥' + str(math.floor(price * (1 - rate)))
    elif currency == 'EUR':
        return '{:.2f}€'.format(price * (1 - rate))
    elif currency == 'USD':
        return '${:.2f}'.format(price * (1- rate))
    else:
        return 'すみません。{}は使用できません'.format(currency)
        
print(discount_price(10000, 0.2))
print(discount_price(100, 0.3, 'EUR'))
print(discount_price(100, 0.4, 'USD'))
print(discount_price(1000, 0.25, 'GBP'))
