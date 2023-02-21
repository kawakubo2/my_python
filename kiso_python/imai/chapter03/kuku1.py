# -*- coding: utf-8 -*-

cnt = 0
for i in range(1, 100):
    for j in range(1, 100):
        cnt += 1
        if i * j > 300:
            break
        print('{:2d}, '.format(i * j), end='')
    print('')
    
print('回数:', cnt)