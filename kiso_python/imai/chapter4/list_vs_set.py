# -*- coding: utf-8 -*-

from random import randint
import time

RAND_MAX = 1000000000
COLLECTION_SIZE = 1000000
LOOP_COUNT = 10000

list1 = []
set1 = set()

# 検証用乱数リスト
rand_list = []

while(len(set1) < COLLECTION_SIZE):
    r = randint(1, RAND_MAX)
    if r not in set1:
        set1.add(r)
        list1.append(r)
        
for i in range(LOOP_COUNT):
    rand_list.append(randint(1, RAND_MAX))
    
print('---< listの検索 >---')
list_ok = 0
list_ng = 0
list_start_time = time.time()

for i in range(LOOP_COUNT):
    r = rand_list[i]
    if r in list1:
        list_ok += 1
    else:
        list_ng += 1

list_end_time = time.time()
print('検索成功: {}'.format(list_ok))
print('検索失敗: {}'.format(list_ng))
print('処理時間: {}'.format(list_end_time - list_start_time))

print('---< setの検索 >---')
set_ok = 0
set_ng = 0
set_start_time = time.time()

for i in range(LOOP_COUNT):
    r = rand_list[i]
    if r in set1:
        set_ok += 1
    else:
        set_ng += 1

set_end_time = time.time()
print('検索成功: {}'.format(set_ok))
print('検索失敗: {}'.format(set_ng))
print('処理時間: {}'.format(set_end_time - set_start_time))