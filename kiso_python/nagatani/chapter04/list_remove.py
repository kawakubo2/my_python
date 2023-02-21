# list_remove.py

names = ['山田', '井上', '太田', '田中', '山田', '佐々木', '山田', '加藤']

name = '山田'

while name in names:
    names.remove(name)

print(names)

# リストの内包表記
names2 = [name for name in names if name != '山田']
print(names2)

names = ['山田', '井上', '太田', '田中', '山田']

indexies = [0, 4]
indexies.reverse()
for pos in indexies:
    del names[pos]

print(names)

list1 = ['A', 'B', 'C', 'D']

list2 = list1[::-1]
print(list2)
print(list1)

nums = [99, 3, -5, 0, 100, 14, 18, 14]
nums2 = sorted(nums, reverse=True)
print(nums2)
print(nums)