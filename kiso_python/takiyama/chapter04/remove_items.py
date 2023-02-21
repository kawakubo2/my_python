names = ["山田", "田中", "太田", "田中", "山田", "鈴木", "山田"]

name = "山田"
while name in names:
    names.remove(name)
    
print(names)

names = ["山田", "田中", "太田", "田中", "山田", "鈴木", "山田"]
names2 = [name for name in names if name != "山田"]
print(names2)
    