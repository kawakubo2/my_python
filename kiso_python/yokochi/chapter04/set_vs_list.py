import random, time

RANDOM_MAX = 1_000_000_000
COLLECTION_SIZE = RANDOM_MAX / 1000
LOOP_COUNT = 10000

list1 = []
set1 = set()
"""
リスト、セットとも100万件の要素を持つ
"""
while len(set1) < COLLECTION_SIZE:
    rand = random.randrange(RANDOM_MAX)
    if rand not in set1:
        set1.add(rand)
        list1.append(rand)

"""
テスト用の乱数のリスト
"""
random_list = []
for i in range(LOOP_COUNT):
    rand = random.randrange(RANDOM_MAX)
    random_list.append(rand)

"""
リストの線形検索
"""
list_start = time.time()
list_ok = 0
list_ng = 0
for i in range(LOOP_COUNT):
    if random_list[i] in list1:
        list_ok += 1
    else:
        list_ng += 1
list_end = time.time()
print(f"処理時間: {list_end - list_start}")
print(f"検索成功: {list_ok}")
print(f"検索失敗: {list_ng}")

"""
セットの検索
"""
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
print(f"検索成功: {set_ok}")
print(f"検索失敗: {set_ng}")
