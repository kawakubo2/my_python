names = ["山田", "井上", "山田", "鈴木", "太田", "山田", "田中", "山田"]

while "山田" in names:
    names.remove("山田")

print(names)

names = ["山田", "井上", "山田", "鈴木", "太田", "山田", "田中", "山田"]

names2 = [name for name in names if name != "山田"]
print(names2)