numbers1 = [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 4, 9, 16, 25, 36, 49, 64]
numbers2 = []
for num in numbers1:
    numbers2.append(num ** 2)
print(numbers2)

numbers3 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers4 = [num ** 2 for num in numbers3]
print(numbers4)

numbers5 = [1, 2, 3, 4, 5, 6, 7, 8]
numbers6 = [num for num in numbers5 if num % 2 == 0]
print(numbers6)

numbers7 = [ 38, 78, 60, 90, 23, 98, 68, 53, 88, 49 ]

m = numbers7[0]
for num in numbers7:
    if num > m:
        m = num

print(f'最大値: {m}')

m = numbers7[0]
for num in numbers7:
    if num < m:
        m = num
        
print(f'最小値: {m}')

total = 0
for num in numbers7:
    total += num # total = total + num
    
print(f'合計: {total}')

total = 0
for num in numbers7:
    if num >= 50:
        total += num
        
print(f'値が50以上の合計: {total}')

total = 0
for num in numbers7:
    if num % 2 == 0:
        total += num
        
print(f'偶数の合計: {total}')

total = 0
for num in numbers7:
    if num % 2 != 0:
        total += num
        
print(f'奇数の合計: {total}')

numbers8 = [
    [ 58, 78, 67, 90, 75 ],
    [ 82, 91, 85, 63, 83 ],
    [ 71, 80, 72, 93, 78 ]
]

print(numbers8[0][0])
print(numbers8[0][1])
print(numbers8[0][2])
print(numbers8[0][3])
print(numbers8[0][4])
print(numbers8[1][0])
print(numbers8[1][1])
print(numbers8[1][2])
print(numbers8[1][3])
print(numbers8[1][4])
print(numbers8[2][0])
print(numbers8[2][1])
print(numbers8[2][2])
print(numbers8[2][3])
print(numbers8[2][4])


"""
58 78 67 90 75
82 91 85 63 83
71 80 72 93 78
"""

for nums in numbers8:
    for num in nums:
        print(f'{num} ', end='')
    print()

# 1行毎の合計を表示
for nums in numbers8:
    total = 0
    for n in nums:
        total += n
    print(total)

numbers9 = [ 11, 8, 5, 4, 12, 7, 3, 10, 9 ]

"""
奇数: 5
偶数: 4
"""
odd_counter = 0
even_counter = 0
for num in numbers9:
    if num % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
        
print(f"奇数: {odd_counter}")
print(f"偶数: {even_counter}")

fruits = ['banana', 'apple', 'orange', 'strawberry', 'pineapple']

max_length = 0
fruit = ''
for f in fruits:
    if len(f) > max_length:
        max_length = len(f)
        fruit = f
        
print(f"配列の中で一番文字数が多い果物は{fruit}です。")
        
fruits.sort(key=lambda f: len(f), reverse=True)
print(fruits)

members = [
    ('山田太郎', 45), ('横山花子', 37), ('田中一郎', 55), ('山本久美子', 48),
    ('星山裕子', 33), ('鈴木次郎', 58), ('佐藤勝男', 50)
]

sorted_members = sorted(members, key=lambda m:m[1])
print(sorted_members)

members2 = [
    ('山田太郎', 170, 78),('田中一郎', 168, 80),('鈴木次郎', 172, 73),
    ('佐藤勝男', 180, 70)
]

sorted_members2 = sorted(members2, key=lambda m:m[2] / (m[1] / 100) ** 2)
print(sorted_members2)

list1 = ['日', '月', '火', '水']
list2 = ['木', '金', '土']

list3 = list1 + list2
print(list3)
print(list1)
print(list2)

list1.extend(list2)
print(list1)

alphabets = ['e', 'f', 'g', 'w', 'a', 'e', 'b', 'c', 'a', 'e', 'd', 'z',
             'q', 'a', 'y', 'c', 'h', 'i', 'w', 'a', 'b', 'v', 'x', 'e']

a_count = 0
for a in alphabets:
    if a == 'a':
        a_count += 1
        
print(f"aの個数: {a_count}")
print(f"aの個数: {alphabets.count('a')}")
print(f"aの個数: {len([a for a in alphabets if a == 'a'])}")

abc_count = 0
for a in alphabets:
    if a in ('a', 'b', 'c'):
        abc_count += 1 

print(f'abcの個数: {abc_count}')

abc_counter = {'a': 0, 'b': 0, 'c': 0 }
for a in alphabets:
    if a in abc_counter:
        abc_counter[a] += 1

for a, count in abc_counter.items():
    print(f"{a}の個数: {abc_counter[a]}")

numbers10 = [ 53, 68, 70, 48, 88, 90, 33, 85, 48, 78]
"""
50未満の数の個数
50以上の数の個数
"""
under50counter = 0
elsecounter = 0

for n in numbers10:
    if n < 50:
        under50counter += 1
    else:
        elsecounter += 1
        
print(f"50未満の数値の数: {under50counter}")
print(f"50以上の数値の数: {elsecounter}")

"""
 0-33
34-66
67-100
"""
a = 0
b = 0
c = 0
for n in numbers10:
    if n <= 33:
        a += 1
    elif n <= 66:
        b += 1
    else:
        c += 1
        
print(f" 0～ 33の個数: {a}")
print(f"34～ 66の個数: {b}")
print(f"67～100の個数: {c}")