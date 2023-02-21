# -*- coding: utf-8 -*-

numbers = [5, 1, 18, 7, 4, 11, 9, 6, 8, 3]

def aggregate(nums):
    total = 0
    max = nums[0]
    min = nums[0]
    cnt = 0
    for n in nums:
        total += n
        if n > max:
            max = n
        if n < min:
            min = n
        cnt += 1
    return (total, total / cnt, max, min, cnt)

my_sum, avg, my_max, my_min, count = aggregate(numbers)

print('合計 =', my_sum)
print('平均 =', avg)
print('最大 =', my_max)
print('最小 =', my_min)
print('件数 =', count)

print('合計 =', sum(numbers))
print('平均 =', sum(numbers) / len(numbers))
print('最大 =', max(numbers))
print('最小 =', min(numbers))
print('件数 =', len(numbers))

# sort 昇順(小さい方から並べ替える) 降順(大きい方から並べ替える)