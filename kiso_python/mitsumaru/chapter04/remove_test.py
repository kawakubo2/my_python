names = ["山田", "井上", "太田", "田中", "山田"]

names.remove("山田")

print(names)

names2 = ["山田", "井上", "太田", "山田", "田中", "山田"]

while "山田" in names2:
    names2.remove("山田")

print(names2)

names3 = ["山田", "井上", "太田", "山田", "田中", "山田"]

# popは末尾から削除
print(names3.pop())
print(names3)

# pop
print(names3.pop(2))
print(names3)

# del
del names3[2]
print(names3)
