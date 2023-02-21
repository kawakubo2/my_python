# names.py

# リスト
names = ['山田太郎', '横山花子', '田中一郎', '山本久美子', '鈴木次郎', '星山裕子', '佐藤勝男']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])
print('---< 逆順 >---')
print(names[-1])
print(names[-2])
print(names[-3])
print(names[-4])
print(names[-5])
print(names[-6])
print(names[-7])

names[0] = '加藤博'
print(names[0])

height = (180, 165, 159, 171, 155)
print(height[0])
print(height[1])
print(height[2])
print(height[3])
print(height[4])

# タプルは追加、更新、削除が出来ない
# height[0] = 185

name = '山田太郎'
print(name[0])
# name[0] = '村'

print(id(100))
n = 100
print(id(n))

for n in names:
    print(n)