# -*- coding: utf-8 -*-

import time

# A - Zの文字を生成
start = time.time()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
counter = {}

for c in alphabets:
    counter[c] = 0

with open('The_Return_of_the_Native_pg122.txt', 'r', encoding='utf_8') as f:
    for line in f:
        for c in line:
            if c in counter:
                counter[c] += 1

                
for alpha in counter.items():
    print('{}:{}'.format(alpha[0], alpha[1]))
    
end = time.time()

print('処理時間: {:.4f}'.format(end - start))