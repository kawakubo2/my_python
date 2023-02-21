# -*- coding: utf-8 -*-

import random
import time
import math

print("SetとListの速度比較")

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = math.floor((left + right) / 2)
        if target > lst[mid]:
            left = mid + 1
        elif target < lst[mid]:
            right = mid - 1
        else:
            return True
    return False

COLLECTION_SIZE = 1000000
RAND_MAX = 1000000000
LOOP_COUNT = 10000

list1 = []
set1 = set()

while len(set1) < COLLECTION_SIZE:
    r = random.randrange(RAND_MAX)
    if r not in set1:
        list1.append(r)
        set1.add(r)
        
rand_list = []

for i in range(LOOP_COUNT):
    r = random.randrange(RAND_MAX)
    rand_list.append(r)
    
print("---< List >---")

list1.sort()
list_start = time.time()
list_ok = 0
list_ng = 0
for i in range(LOOP_COUNT):
    if binary_search(list1, rand_list[i]):
        list_ok += 1
    else:
        list_ng += 1

list_end = time.time()
print("ok: {}, ng: {}, 処理時間: {}".format(list_ok, list_ng, list_end - list_start))

print("---< Set >---")

set_start = time.time()
set_ok = 0
set_ng = 0
for i in range(LOOP_COUNT):
    if rand_list[i] in set1:
        set_ok += 1
    else:
        set_ng += 1
        
set_end = time.time()
print("ok: {}, ng: {}, 処理時間: {}".format(set_ok, set_ng, set_end - set_start))
