list1 = [1, 2, 3, 4, 5]
list2 = [n + '賞' for n in ('金', '銀', '銅')]
print(list2)
for w in list('日月火水木金土'):
    print(w + '曜日')

str1 = 'Python,Java,Go,Rust,C++'
list3 = str1.split(',')
print(list3)
str2 = '<br />'.join(list3)
print(str2)

list4 = list('abcdefg')
list5 = list4[:3]
list6 = list4[3:5]
list7 = list4[5:]
print(list5)
print(list6)
print(list7)

email = 'tomo.kawakubo@gmail.com'
local = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print('ローカル部:{} ドメイン部:{}'.format(local, domain))

list8 = list('abcdef')
print(list8)
list9 = list8[:]
list9[0] = 'A'
print(list8)
print(list9)
list10 = list8[-3:]

data = [
    [1, 2, 3],
    [4, 5, 6, 7],
    8,
    [9, 10, [11, 12, [13, 14]], 15],
]

def my_len(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += my_len(item)
        else:
            count += 1
    return count

print(my_len(data))

b = ['a', 'b', 'c', 'c', 'a', 'b', 'a']

while 'a' in b:
    b.remove('a')

print(b)
 

d = list('ABCDEFG')
print(d)
d[1:3] = ['X', 'Y', 'Z']
print(d)
d[1:4] = []
print(d)
d[1:1] = ['B', 'C']
print(d)

data = ['鈴木', '田中', '井上', '加藤']
data2 = data[:] # data.copy()
data2[1:2] = ['佐々木', '高島']
print(data2)
print(data)

import copy

data3 = [1, 2, [3, 4], 5, 6]
data4 = copy.deepcopy(data3)

data4[2][0] += 10
print(data4)
print(data3)

data4[0] = 100
print(data4)
print(data3)

data5 = [1, 2, [3, 4, [5, 6]], [7, [8, 9]], 10]
data6 = copy.deepcopy(data5)
data6[2][2][0] = 100
print(data6)
print(data5)

def plus10(nums):
    for i in range(len(nums)):
        nums[i] += 10

data7 = [1, 2, 3, 4, 5]
plus10(data7)
print(data7)

class Person:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        for n in self.score:
            print('{} '.format(n), end='')
        print('')

str1 = 'abcdefg'

list1 = ['x', 'y', 'z']
for c in str1:
    list1.append(c) # list += [c]

print(list1)