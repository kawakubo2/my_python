# -*- coding: utf-8 -*-

names = ['山田', '佐藤', '山田', '佐々木', '山田', '加藤', '鈴木', '山田']

n = '山田'

while n in names:
    names.remove(n)
    
print(names)

names = ['山田', '佐藤', '山田', '佐々木', '山田', '加藤', '鈴木', '山田']

while True:
    try:
        index = names.index(n)
        del names[index]
    except ValueError:
        break

print(names)

names = ['山田', '佐藤', '山田', '佐々木', '山田', '加藤', '鈴木', '山田']

names2 = [name for name in names if name != n]

print(names2)

print(names)

pixels = list(range(1, 17))
print(pixels)
left = pixels[0::4]
print(left)
del pixels[0::4]
print(pixels)

pixels2 = []
cnt = 0
for i, p in enumerate(pixels):
    pixels2.append(p)
    if i % 3 == 2:
        pixels2.append(left[cnt])
        cnt += 1
    
    
print(pixels2)

nums = [1, 2, 3, 4, 5, 6, 7]
nums.reverse()
print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
nums2 = nums[::-1]
print(nums2)
print(nums)


def aggregate_func(nums):
    total = 0
    cnt = 0
    max = nums[0]
    min = nums[0]
    for n in nums:
        total += n
        cnt += 1
        if n > max:
            max = n
        if n < min:
            min = n
    return {'sum': total, 'avg': total / cnt, 'max': max, 'min': min, 'count': cnt}

result = aggregate_func(nums)
print(result)

  