nums1 = list(range(1, 101))

nums2 = []
for n in nums1:
    nums2.append(n / 100)

total = 0
for n in nums2:
    total += (n/100)

print(total)
