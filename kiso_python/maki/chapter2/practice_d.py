# -*- coding: utf-8 -*-

import random

janken = ['パー', 'チョキ', 'グー']

win = 0
lose = 0
even = 0

for n in range(10):
    print('\n\n' + str(n+1) + '回目' )
    hand = int(input('1.パー 2.チョキ 3.グー : ')) - 1
    comp_hand = random.randrange(len(janken))
    
    print('あなた-> {} コンピュータ -> {}'.format(janken[hand], janken[comp_hand]))
    if (comp_hand + 1) % 3 == hand:
        print('あなたの勝ち')
        win += 1
    elif (hand + 1) % 3 == comp_hand:
        print('あなたの負け')
        lose += 1
    else:
        print('引き分け')
        even += 1
        
print('勝ち={}, 負け={}, 引き分け={}'.format(win, lose, even))