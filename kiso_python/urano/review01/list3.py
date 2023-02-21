list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# スライス
list2 = list1[2:5] # ['C', 'D', 'E' ]
print(list2)

list3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# C, D, Eを削除して、削除した位置にX, Yを格納する
list3[2:5] = ['X', 'Y']
print(list3)

list4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# C, D, Eを削除
list4[2:5] = []
print(list4)

list5 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# BとCの間にX,Y,Zを挿入する
list5[2:2] = ['X', 'Y', 'Z']
print(list5)
