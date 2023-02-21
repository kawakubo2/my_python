nums1 = [1, 3, 7, 10, 9, 15, 20, 30]
nums2 = [n for n in nums1 if n % 3 == 0]
print(nums2)

names = ["山田", "田中", "鈴木", "山田", "加藤", "山田"]
n = "山田"
"""
while n in names:
    names.remove(n)
"""

names2 = []
for name in names:
    if name != n:
        names2.append(name)  
print(names2)

names3 = [name for name in names if name != n]
print(names3)