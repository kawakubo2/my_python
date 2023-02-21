import random
import time

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return True
    return False

RAND_MAX = 1_000_000_000
COLLECTION_SIZE = RAND_MAX // 1000
LOOP_COUNT = 10000

list1 = []
set1 = set()
random_list = []

while len(set1) < COLLECTION_SIZE:
    r = random.randrange(RAND_MAX)
    if r in set1:
        continue
    list1.append(r)
    set1.add(r)

while len(random_list) < LOOP_COUNT:
    random_list.append(random.randrange(RAND_MAX))

list1.sort()

print('--- リストの2分探索 ---')
list_start = time.time()
list_ok = 0
list_ng = 0
for i in range(LOOP_COUNT):
    if binary_search(list1, random_list[i]):
        list_ok += 1
    else:
        list_ng += 1

list_end = time.time()
print(f'成功件数: {list_ok} 失敗件数: {list_ng}')
print(f'処理時間: {list_end - list_start}')

print('--- 集合の検索 ---')
set_start = time.time()
set_ok = 0
set_ng = 0
for i in range(LOOP_COUNT):
    if random_list[i] in set1:
        set_ok += 1
    else:
        set_ng += 1

set_end = time.time()
print(f'成功件数: {set_ok} 失敗件数: {set_ng}')
print(f'処理時間: {set_end - set_start}')

