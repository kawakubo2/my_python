# set_vs_list.py
import random, time

RAND_MAX = 10_000_000_000
COLLECTION_SIZE = RAND_MAX / 1000
LOOP_COUNT = 10_000

# 初期化処理
set1 = set()
list1 = []

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
        else:
            return True
    return False

while len(set1) < COLLECTION_SIZE:
    r = random.randrange(RAND_MAX)
    if r not in set1:
        set1.add(r)
        list1.append(r)

# print(f"set1のsize: {len(set1)} list1のサイズ: {len(list1)}")

# テスト用の乱数のリスト
random_list = []
while len(random_list) < LOOP_COUNT:
    r = random.randrange(RAND_MAX)
    random_list.append(r)

list1.sort()
print("---< リストの二分探索 >---")
list_start = time.time()
list_ok = 0
list_ng = 0
for i in range(LOOP_COUNT):
    if binary_search(list1, random_list[i]):
        list_ok += 1
    else:
        list_ng += 1
list_end = time.time()

print(f"処理時間: {list_end - list_start}")
print(f"成功件数: {list_ok}")
print(f"失敗件数: {list_ng}")

print("---< Setの検索 >---")
set_start = time.time()
set_ok = 0
set_ng = 0
for i in range(LOOP_COUNT):
    if random_list[i] in set1:
        set_ok += 1
    else:
        set_ng += 1
set_end = time.time()

print(f"処理時間: {set_end - set_start}")
print(f"成功件数: {set_ok}")
print(f"失敗件数: {set_ng}")