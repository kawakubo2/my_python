# -*- coding: utf-8 -*-

import random

janken = ['グー', 'チョキ', 'パー']


def judge(hand1, hand2, names):
    print(names[0] + ':' + hand1)
    print(names[1] + ':' + hand2)
    if ((janken.index(hand1) + 1) % len(janken)) == janken.index(hand2):
        return names[0] + 'さんの勝ち'
    elif hand1 == hand2:
        return '引き分け'
    else:
        return names[1] + 'さんの勝ち'
    
print(judge(janken[random.randrange(len(janken))], janken[random.randrange(len(janken))], ('太郎', '花子')))
