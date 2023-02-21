list1 = ['春', '夏']
list2 = ['秋', '冬']
list3 = list1 + list2
print(list1)
print(list2)
print(list3)
list4 = list1 * 3
print(list4)

list5 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
list6 = list5[2:5]
print(list5)
print(list6)
print('削除')
list5[2:5] = []
print(list5)
list5 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print('置換')
list5[2:5] = ['X', 'Y']
print(list5)
print('挿入')
list5 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
list5[2:2] = ['X', 'Y', 'Z']
print(list5)

w = '日:月:火:水:木:金:土'
weeklist = w.split(':')
print(weeklist)

print(weeklist.index('水'))
if '地' in weeklist:
    print(weeklist.index('地'))

list5.append('H')
list5.append('I')
print(list5)

list5[5:5] = ['W']
print(list5)

c1 = list5.pop()
print(f"list5={list5}")
print(f"c1={c1}")

list5.insert(2, 'I')
print(list5)
list5.extend(['X', 'X'])
print(list5)
list5 = [e for e in list5 if e != 'X'] # 内包表記
print(list5)
# list6 = [w + '曜日' for w in weeklist]
list6 = []
for w in weeklist:
    list6.append(w + '曜日')
print(list6)

numbers = [1, 2, 3, 4, 5, 6]
total = sum([n ** 2 for n in numbers if n % 2 == 0])
"""
total = 0
for n in numbers:
    if n % 2 == 0:
        total += n ** 2
"""
print(f"合計: {total}")

names = ['山田', '田中', '鈴木']
names2 = [name + 'さん' for name in names]
print(names2)

names3 = ['山田\n', '田中\n', '鈴木\n']
names4 = [ name.rstrip('\n') for name in names3]
print(names4)

names5 = ['山田', '鈴木', '田中', '佐藤', '山田', '鈴木', '山田']

 # while '山田' in names5:
 #   names5.remove('山田')
 
names6 = [name for name in names5 if name != '山田']

print(names6)

members = ['A001', 'A003', 'C002', 'D002', 'E001', 'A005']

member_id = 'D002'
if member_id in members:
    pos = members.index(member_id)
    # members.pop(pos)
    members2 = members.pop(pos)
print(members2)

weeklist = ['日', '月', '火', '水', '木', '金', '土']

"""
import math
for i in range(math.floor(len(weeklist) / 2)):
    temp = weeklist[len(weeklist) - 1 - i]
    weeklist[len(weeklist) - 1 - i] = weeklist[i]
    weeklist[i] = temp
"""

print(weeklist)
    