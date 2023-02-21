list1 = list()

list2 = []

list2.append(1)
list2.append(2)
list2.append(4)
list2.append(8)

print(list2)

print('要素数 =', len(list2))

list2.pop(2)

print(list2)
print('要素数 =', len(list2))

list2.pop()
print(list2)
print('要素数 =', len(list2))

list2.append(4)
list2.append(8)
print(list2)
print('要素数 =', len(list2))

name = "山田太郎"
age = 38
height = 168
weight = 65

print(name + "さんの年齢は" + str(age) + "歳です")
print("%sさんの年齢は%d歳です" % (name, age))
print("{}さんの年齢は{}歳です".format(name, age))
print(f"{name}さんの年齢は{age}歳です")

print(f"{name}さんのBMI値は{weight / (height/100) ** 2:.2f}です")
print("{}さんのBMI値は{:.2f}です".format(name, weight / (height/100) ** 2))
print("%sさんのBMI値は%.2fです" % (name, weight / (height/100) ** 2))

