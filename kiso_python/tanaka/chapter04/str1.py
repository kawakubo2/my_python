from turtle import width


x = "123"
y = 123.0

print(type(x))
print(type(y))

s1 = "kokohagoko"
print(s1.count("ko"))

url1 = 'http://example.com'
url2 = 'https://example2.co.jp'

print(url1.startswith('https://'))
print(url2.startswith('https://'))

ext1 = 'abc.py'
ext2 = 'xyz.java'

print(ext1.endswith('.py'))
print(ext2.endswith('.py'))

s2 = 'tomo.kawakubo@gmail.com'
print(s2[2:5])
print(s2.find('@'))
print('@' in s2)

local = s2[:s2.find('@')]
domain = s2[s2.find('@')+1:]

print(f"ローカル部: {local}")
print(f"ドメイン部: {domain}")
print(f"メールアドレス: {s2}")

langs = ['Python', 'SQL', 'Java', 'C#', 'Rust']
print(','.join(langs))
s3 = 'バナナ,オレンジ,グレープ,パイナップル'
s4 = 'Banana,Orange,Grape,Pineapple'
fruits_dict = {}
for ja, en in zip(s3.split(','), s4.split(',')):
    fruits_dict[ja] = en
print(fruits_dict)

s5 = 'JavaScript'
print(s5.upper())
print(s5.lower())
print(s5)

s6 = 'http://example.com'
print(s6.removeprefix('http://'))


s7 = 'http://'
pos1 = s6.find(s7)
print(s6[pos1 + len(s7):])

s8 = 'abc.py'
print(s8.removesuffix('.py'))

s9 = 'learning robot in python'
print(s9.title())

print('-' * 20)
a1 = ['Python', 'JavaScript', 'C', 'C++', 'Java']
for s10 in a1:
    print(s10.center(20, '-'))

name = '山田太郎'
age = 32
print('---< 方法1 >---')
print(name + 'さんの年齢は' + str(age) + '歳です。')

print('---< 方法2 >---')
print('%sさんの年齢は%d歳です。' % (name, age))

print('---< 方法3 >---')
print('{}さんの年齢は{}歳です。'.format(name, age))

print('---< 方法4 >---')
print(f"{name}さんの年齢は{age}歳です。")

weight = 88
height = 180

print("%sさんのbmi値は%.2f" % (name, weight / (height / 100) ** 2))
print("{}さんのbmi値は{:.2f}".format(name, weight / (height / 100) ** 2))
print(f"{name}さんのbmi値は{weight / (height / 100) ** 2:.2f}")

print('{1:}さんですよね。私は{0:}です。...あれ？{1:}さんですよね。'.format('川久保', '田中'))

number1 = 12345.6789012
print("数値:{:,.3f}".format(number1))
print(f"数値:{number1:,.3f}")