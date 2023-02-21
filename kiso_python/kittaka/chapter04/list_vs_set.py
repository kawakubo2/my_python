import random, time

RAND_MAX = 1_000_000_000 # 10億
COLLECTION_SIZE = RAND_MAX / 1000 # 100万
LOOP_COUNT = 10_000 # テスト回数

list1 = []
set1 = set()

#######################################
# リストと集合に同じ要素を100万件格納
#######################################

while len(set1) < COLLECTION_SIZE:
    r = random.randint(1, RAND_MAX)
    if r not in set1:
        list1.append(r)
        set1.add(r)
        
#######################################
# 1万件のテスト用乱数の準備
#######################################

rand_list = []
for _ in range(LOOP_COUNT):
    rand_list.append(random.randint(1, RAND_MAX))

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return True
    return False
    
    
#######################################
# リストの二分探索(binary search)
#######################################
list1.sort()    

list_start = time.time()
list_ok = 0 # 検索成功用のカウンタ
list_ng = 0 # 検索失敗用のカウンタ

for r in rand_list:
    if binary_search(list1, r):
        list_ok += 1
    else:
        list_ng += 1
        
list_end = time.time()
print(f"検索成功: {list_ok}")
print(f"検索失敗: {list_ng}")
print(f"処理時間: {list_end - list_start}")

#######################################
# 集合の検索
#######################################
    
set_start = time.time()
set_ok = 0 # 検索成功用のカウンタ
set_ng = 0 # 検索失敗用のカウンタ

for r in rand_list:
    if r in set1:
        set_ok += 1
    else:
        set_ng += 1
        
set_end = time.time()
print(f"検索成功: {set_ok}")
print(f"検索失敗: {set_ng}")
print(f"処理時間: {set_end - set_start}")