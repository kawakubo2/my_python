import random, time

RANDOM_MAX = 100_000_000 # 1憶
COLLECTION_SIZE = RANDOM_MAX / 1000
LOOP_COUNT = 10_000

li = []
st = set()

while len(st) < COLLECTION_SIZE:
    r = random.randrange(RANDOM_MAX) + 1 # 1から1憶までの乱数を生成

    if r not in st:
        li.append(r)
        st.add(r)
        
print(f"リストの件数: {len(st)}")
print(f"集合の件数: {len(st)}")

random_list = []
while len(random_list) < LOOP_COUNT:
    r = random.randrange(RANDOM_MAX) + 1 # 1から10憶までの乱数を生成
    random_list.append(r)
    
print('---< listの線形検索 ---')
list_start = time.perf_counter()
list_ok = 0
list_ng = 0
for ra in random_list:
    if ra in li:
        list_ok += 1
    else:
        list_ng += 1
list_end = time.perf_counter()
list_diff = list_end - list_start
print(f"成功件数: {list_ok}")
print(f"失敗件数: {list_ng}")
print(f"処理時間: {list_diff}")
    
print('---< setの線形検索 ---')
set_start = time.perf_counter()
set_ok = 0
set_ng = 0
for ra in random_list:
    if ra in st:
        set_ok += 1
    else:
        set_ng += 1
set_end = time.perf_counter()
set_diff = set_end - set_start
print(f"成功件数: {set_ok}")
print(f"失敗件数: {set_ng}")
print(f"処理時間: {set_diff}")