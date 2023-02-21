import random, time

RAND_MAX = 1_000_000_000           # 10億
COLLECTION_SIZE = RAND_MAX / 1000  # 100万
LOOP_COUNT = 10_000

##############################################
# リストと集合の準備
##############################################

list1 = []
set1 = set()

while len(set1) < COLLECTION_SIZE:
    r = random.randint(1, RAND_MAX)
    if r not in set1:
        set1.add(r)
        list1.append(r)

##############################################
# ループ回数分の乱数を格納したリストの生成
##############################################

rand_list = []
for _ in range(LOOP_COUNT):
    rand_list.append(random.randint(1, RAND_MAX))
    
##############################################
# リストの二分検索
##############################################

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
print(f"成功件数: {list_ok}")
print(f"失敗件数: {list_ng}")
print(f"処理時間: {list_end - list_start}")
    
##############################################
# Setの検索
##############################################

set_start = time.time()
set_ok = 0
set_ng = 0

for i in range(LOOP_COUNT):
    if rand_list[i] in set1:
        set_ok += 1
    else:
        set_ng += 1
        
set_end = time.time()
print(f"成功件数: {set_ok}")
print(f"失敗件数: {set_ng}")
print(f"処理時間: {set_end - set_start}")
print(f"要素数: {COLLECTION_SIZE}")