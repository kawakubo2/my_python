list1 = [1, 2, 4, 8, 16, 32, 64]

print(list1[len(list1) - 1])
print(list1[-1])

t1 = ("赤", "黒", "緑")
l1 = list(t1)
print(l1)
l1[1] = "白"
print(l1)

print(t1)

print(id(3))
x = 3
print(id(3))
x += 1
print(id(x))
print(id(3))