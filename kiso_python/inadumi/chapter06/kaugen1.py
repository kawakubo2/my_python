# -*- coding: utf-8 -*-

import random

f = open('kakugen.txt', 'r', encoding='utf_8')
lines = f.readlines()

while True:
    kakugen = lines[random.randrange(len(lines))]
    print(kakugen.rstrip('\n'))
    ans = input('続けますか y:続ける n:中止する: ')
    if (ans != 'y'):
        break
    