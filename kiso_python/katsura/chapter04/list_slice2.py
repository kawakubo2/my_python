list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

print('---< 削除 >---')
list1[2:5] = []
print(list1)

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
print('---< 置換 >---')
list1[2:5] = ['Q', 'R', 'S', 'T']
print(list1)

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
print('---< 挿入 >---')
list1[2:2] = ['Q', 'R', 'S', 'T']
print(list1)

dates = ['2021-10-22', '2021/10/22', '2021.10.22']

import re
pattern = r'(\d{4})[\/\.\-](\d{1,2})[\/\.\-](\d{1,2})'
reg = re.compile(pattern)
for d1 in dates:
    temp = reg.sub(r'\1,\2,\3', d1).split(',')
    print([int(d) for d in temp])
