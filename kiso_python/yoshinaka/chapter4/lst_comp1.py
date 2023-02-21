lst = []

for num in range(0, 21, 2):
    lst.append(num ** 2)

print(lst)

lst2 = [num ** 2 for num in range(0, 21, 2)]
print(lst2)

weeks = [w + '曜日' for w in '日月火水木金土']
print(weeks)

nums1 = [1, 3, 7, 10, 9, 15, 20, 30]
nums2 = []
for n in nums1:
    if n % 3 == 0:
        nums2.append(n)

print(nums2)
nums3 = [n for n in nums1 if n % 3 == 0]
print(nums3)