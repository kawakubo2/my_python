list1 = ["A", "B", "C", "D", "E", "F", "H", "I"]

list2 = list1[2:5]
print(f"list1={list1}")
print(f"list2={list2}")
list3 = list1[0::2]
print(f"list1={list1}")
print(f"list3={list3}")
list4 = list1[-5:-2]
print(f"list1={list1}")
print(f"list4={list4}")
list5 = list1[:]
print(f"list1={list1}")
print(f"list5={list5}")

print('--- 置換 ---')
list1[2:5] = ["X", "Y"]
print(list1)

list1 = ["A", "B", "C", "D", "E", "F", "H", "I"]

print('--- 削除 ---')
list1[2:5] = []
print(list1)

list1 = ["A", "B", "C", "D", "E", "F", "H", "I"]

print('--- 追加 ---')
list1[2:2] = ["X", "Y"]
print(list1)

list1 = ["A", "B", "C", "D", "E", "F", "H", "I", "J", "K", "L", "M", "N", "O", "P",
         "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(list1[:4]), 
print(list1[4:])

start = 0
size = 3
while True:
    if start + size >= len(list1):
        print(list1[start:len(list1)])
        break
    print(list1[start:start+size])
    start += size