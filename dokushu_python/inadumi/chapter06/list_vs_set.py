import random
import time

RAND_MAX = 1_000_000_000
COLLECTION_SIZE = RAND_MAX / 1000
LOOP_COUNT = 10000

list1 = []
set1 = set()
rand_list = []

def binary_search(list1, target):
    left = 0
    right = len(list1) - 1
    while left <= right:
        mid = (left + right) // 2
        if list1[mid] > target:
            right = mid - 1
        elif list1[mid] < target:
            left = mid + 1
        else:
            return True
    return False

while len(set1) < COLLECTION_SIZE:
    r = random.randrange(RAND_MAX)
    if r not in set1:
        # list.append(r)をコメントアウトしていた！
        list1.append(r)
        set1.add(r)

while len(rand_list) < LOOP_COUNT:
    r = random.randrange(RAND_MAX)
    rand_list.append(r)
list_sort_start = time.time()
# list1.sort()
list_sort_end = time.time()
print('100万件のリストのsortに要する時間:' + str(list_sort_end - list_sort_start))
print('---< listの線形検索 >---')
list_start = time.time()
list_ok = 0
list_ng = 0
for i in range(LOOP_COUNT):
    rand = rand_list[i]
    if rand in list1:
        list_ok += 1
    else:
        list_ng += 1
list_end = time.time()
print('成功件数: {}'.format(list_ok))
print('失敗件数: {}'.format(list_ng))
print('処理時間:{}'.format(list_end - list_start))

print('---< setの検索 >---')
set_start = time.time()
set_ok = 0
set_ng = 0
for i in range(LOOP_COUNT):
    rand = rand_list[i]
    if rand in set1:
        set_ok += 1
    else:
        set_ng += 1
set_end = time.time()
print('成功件数: {}'.format(set_ok))
print('失敗件数: {}'.format(set_ng))
print('処理時間:{}'.format(set_end - set_start))


