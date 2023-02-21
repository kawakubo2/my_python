# -*- coding: utf-8 -*-
score = []
with open('score.txt', 'r') as f:
    for n in f:
        score.append(int(n.rstrip('\n')))

total = 0
for n in score:
    print(str(n) + ' ', end='')
    total += n
print('')
print('合計', total)

total = 0
for i in range(len(score)):
    print(str(score[i]) + ' ', end='')
    total += score[i] # total = total + score[i]
print('')
print('合計', total)