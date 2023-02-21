# -*- coding: utf-8 -*-

suit = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = [(s, r) for s in suit for r in rank]
print(cards)