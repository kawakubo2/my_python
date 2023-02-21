# -*- coding: utf-8 -*-

names = ['山田','井上', '太田', '田中', '山田']

while('山田' in names):
    names.remove('山田')

print(names)

names = ['山田','井上', '太田', '田中', '山田']

del names[3]

print(names)

names = ['山田','井上', '太田', '田中', '山田']

del names[1:4]

print(names)

weekdays =['日','月','火','水','木','金','土']
weekdays.reverse();
print(weekdays)

nums = [-1, 9, 4, 10]

total = 0
for n in nums:
    total += n
    
print("合計:{}".format(total))

print("合計:{}".format(sum(nums)))
print("最大値:{}".format(max(nums)))
print("最小値:{}".format(min(nums)))

nums = [99, 3, -5, 0, 100, 14, 18, 14]

nums.sort()
print(nums)

nums = [99, 3, -5, 0, 100, 14, 18, 14]

nums.sort(reverse=True)
print(nums)

nums = [99, 3, -5, 0, 100, 14, 18, 14]

nums2 = sorted(nums)
print(nums)
print(nums2)

