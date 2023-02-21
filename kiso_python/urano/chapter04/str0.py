# str0.py

s1 = 'Python'
print(s1.upper())

s2 = 'PYTHON'
print(s2.lower())

s3 = 'kokohadoko'
print(s3.count('o'))
print(s3.count('ko'))

s4 = 'abcdefg.py'
print(s4.endswith('.py'))
s5 = 'xyz.java'
print(s5.endswith('.py'))

s6 = 'tomo.kawakubo@gmail.com'
pos1 = s6.find('@')
print(pos1)
local = s6[:pos1]
domain = s6[pos1 + 1:]
print('ローカル部: ' + local)
print('ドメイン部: ' + domain)

langs = ['Python', 'Java', 'C#', 'TypeScript', 'PHP']

s7 = ",".join(langs)
print(s7)

s8 = "バナナ,アップル,オレンジ,グレープ"

list1 = s8.split(',')
print(list1)

s9 = 'kokohadoko'
s10 = s9.replace('ko', '---')
print(s10)

s11 = 'http://example.com'
print(s11.startswith('https'))

s12 = 'https://haru-idea.jp'
print(s12.startswith('https'))

s13 = s12.removeprefix('https://')
print(s13)

s14 = 'str0.py'
s15 = s14.removesuffix('.py')
print(s15)
