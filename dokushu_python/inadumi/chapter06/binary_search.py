import random
import time

NUM = 10000000
LOOP_COUNT = 10000

rand_list = []
for i in range(LOOP_COUNT):
    rand_list.append(random.randrange(NUM * 1000))

start = time.time()

list1 = []

for i in range(NUM):
    list1.append(random.randrange(NUM * 1000))

list1.sort()

# for n in list1:
#     print(n)

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid_index = (left + right) // 2
        if target > nums[mid_index]:
            left = mid_index + 1
        elif target < nums[mid_index]:
            right = mid_index - 1
        else:
            return True
    return False

target = random.randrange(NUM)

end = time.time()

ok = 0
ng = 0

for i in range(LOOP_COUNT):
    if binary_search(list1, rand_list[i]):
        ok += 1
    else:
        ng += 1

ellapsed_time = end - start
print('処理時間: {}'.format(ellapsed_time))
print('成功：{} 失敗: {}'.format(ok, ng))

import bisect

for i in range(LOOP_COUNT):
    bisect.insort(list1, rand_list[i])

def test(nums):
    for i in range(len(nums) - 1):
        if (nums[i] > nums[i + 1]): 
            return False
    return True

if test(list1):
    print('ソート検証成功')
else:
    print('ソート検証失敗')