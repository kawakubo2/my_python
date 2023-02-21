import math

radius = [1.23, 3.52, 8.21, 2.86, 5.39]

circle_area_total = sum([r ** 2 * math.pi for r in radius])
print(circle_area_total)

circle_area2 = []
for r in radius:
    circle_area2.append(r ** 2 * math.pi)
print(sum(circle_area2))

nums1 = [1, 3, 7, 10, 9, 15, 20, 30]

nums2 = []
for n in nums1:
    if n % 3 == 0:
        nums2.append(n)
print(nums2)

nums3 = [n for n in nums1 if n % 3 == 0]
print(nums3)