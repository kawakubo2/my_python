import random, time

RAND_MAX = 1_000_000_000
COLLECTION_SIZE = RAND_MAX / 1000
LOOP_COUNT = 10000

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > lst[mid]:
            left = mid + 1
        elif target < lst[mid]:
            right = mid - 1
        else:
            return True
    return False

set1 = set()
list1 = []
while len(set1) < COLLECTION_SIZE:
    rand = random.randrange(RAND_MAX)
    if rand not in set1:
        set1.add(rand)
        list1.append(rand)

random_list = []
for _ in range(LOOP_COUNT):
    random_list.append(random.randrange(RAND_MAX))

list1.sort()
print('---< リストの二分検索 >---')
list_ok = 0
list_ng = 0

list_start = time.time()

for i in range(LOOP_COUNT):
    if binary_search(list1, random_list[i]): 
        list_ok += 1
    else:
        list_ng += 1

list_end = time.time()
print(f"成功件数: {list_ok}")
print(f"失敗件数: {list_ng}")
print(f"処理時間: {list_end - list_start}")

print('---< Setの検索 >---')
set_ok = 0
set_ng = 0

set_start = time.time()

for i in range(LOOP_COUNT):
    if random_list[i] in set1:
        set_ok += 1
    else:
        set_ng += 1

set_end = time.time()
print(f"成功件数: {set_ok}")
print(f"失敗件数: {set_ng}")
print(f"処理時間: {set_end - set_start}")