# str0.py

# countメソッド
s1 = "kokohadoko"
print(s1.count('o'))
print(s1.count('ko'))

# startswith, endswith
s2 = 'https://haru-idea.jp'
print(s2.startswith('https'))
s3 = 'foo.py'
print(s3.endswith('.py'))

# findメソッドとスライス
s4 = 'tomo.kawakubo@gmail.com'
pos = s4.find('@')
if pos > -1:
    print(f"ローカル部: {s4[:pos]}")
    print(f"ドメイン部: {s4[pos+1:]}")

# splitメソッド
local, domain = s4.split('@')
print(f'ローカル部: {local}')
print(f'ドメイン部: {domain}')

s5 = 'Python,Java,TypeScript,C#,C++'
list1 = s5.split(',')
print(list1)

# joinメソッド
s6 = "---".join(list1)
print(s6)

# upper, lowerメソッド
s7 = "JavaScript"
print(s7.upper())
print(s7.lower())

# capitalizeメソッド
s8 = 'python'
print(s8.capitalize())

# titleメソッド
s9 = 'the c++ programming language'
print(s9.title())

s10 = 'kokohadoko'
print(s10.replace('ko', '###'))
print(s10.replace('o', ''))

s11 = 'https://haru-idea.jp'
# s11.removeprefix('https://')
s12 = 'abc.java'
# s12.removesuffix('.java')

s13 = '川久保智晴'

for c in s13:
    print(f"{c}:{ord(c)}")

for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(f"{c}:{ord(c)}")

for c in "ァアィイゥウェエォオ":
    print(f"{c}:{ord(c)}")

s14 =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
size = len(s14) // 5
print(s14[size * 0:size * 1])
print(s14[size * 1:size * 2])
print(s14[size * 2:size * 3])
print(s14[size * 3:size * 4])
print(s14[size * 4:size * 5])
print(s14[size * 5:size * 6])

max = len(s14) // 5 if len(s14) % 5 == 0 else len(s14) // 5 + 1
for i in range(max):
    print(s14[size*i: size*(i+1)])

s15 = s14[:]
print(s15)
print(f"{id(s14)}:{id(s15)}")
s16 = s14[::-1]
print(s16)

# count
s17 = "tomo.kawakubo@gmail.com\nBcc:hacker@example.com"
print(s17.count('@'))

name = '山田太郎'
age =  38
# print書き方
# (1)
print(name + 'さんの年齢は' + str(age) + '歳です。')
# (2)
print('%sさんの年齢は%d歳です。' % (name, age))
# (3) {} <--- プレイスホルダ
print('{}さんの年齢は{}歳です。'.format(name, age))
# (4) \を含む場合は使用できない
print(f'{name}さんの年齢は{age}歳です。')

def bmi(weight, height):
    return weight / (height / 100) ** 2

w = 75
h = 172
print('%sさんのBMI値は%.2f' % (name, bmi(w,h)))
print('{1}さんのBMI値は{0:.2f}'.format(bmi(w, h), name))
print(f'{name}さんのBMI値は{bmi(w, h):.2f}')

print('{1}さん、私は{0}です。・・・あれ？{1}さんですよね。'.format('山田', '鈴木'))
