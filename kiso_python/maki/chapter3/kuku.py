# -*- coding: utf-8 -*-

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        cnt += 1
        if i * j > 30:
            break
        print("{}*{}={:2d} ".format(i, j, i * j), end='')
    print('')
    
print('回った回数:', cnt)