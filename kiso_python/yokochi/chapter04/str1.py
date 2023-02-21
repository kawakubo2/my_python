s1 = 'kokohadoko'
s2 = '12900000130'

s3 = 'SYNxxxxxxxeuieytewuACKeiwut3229SYN039r08ACK';

print(s1.count('o'))
print(s1.count('ko'))

print(s2.count('0'))

print(s3.count('SYN'))

url = 'https://haru-idea.jp'
url2 = 'http://example.com'
print(url.startswith('https'))
print(url2.startswith('https'))

file1 = 'abc.py'
file2 = 'xyz.java'

print(file1.endswith('.py'))
print(file2.endswith('.py'))

s1 = 'このプログラムはPythonで作られています。'
s2 = 'このプログラムはC#で作られています'

print(s1.find('Python')) # 見つかった場合は検索文字列の最初のインデックを
print(s2.find('Python')) # 見つからない場合は-1を返す

if 'Python' in s1:
    print(s1[s1.find('Python'):])

email = 'tomo.kawakubo@gmail.com' # ローカル部@ドメイン部

local = email[0:email.find('@')]
domain = email[email.find('@') + 1:]

print(f'ローカル部: {local} ドメイン部: {domain}')

ary = email.split('@')
print(f'ローカル部: {ary[0]} ドメイン部: {ary[1]}')

langs = ['Python', 'Java', 'C++', 'TypeScript', 'Go', 'Rust']

lang_str = '\t'.join(langs)
print(lang_str)

s2 = 'JavaScript'

print(f'{s2.lower()} {s2.upper()}')

s3 = 'prince'
print(s3.capitalize())

s4 = 'learn microservices with spring boot'
print(s4.title())

name = '川久保智晴'

for c in name:
    print(f'{c}の文字コードは{ord(c)}')

lst = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9, 9, 10, 11, 12, 12, 13]

# リストを5個に分解したい
span = len(lst) // 5
result = []
i = 0
for n in range(5):
    result.append(lst[i : i + span])
    i += span

print(result)

name = '山田太郎'
age = 38
weight = 70
height = 170

print(name + 'さんの年齢は' + str(age) + '歳です。')
print('%sさんの年齢は%d歳です。' % (name, age))
print('{}さんの年齢は{}歳です。'.format(name, age))
print(f'{name}さんの年齢は{age}歳です。')

print('{1:}さんの年齢は{0:}歳です。'.format(age, name))
name2 = '横山花子'
print('{1:}さん。私は{0:}です。...{1:}さんですよね(;^_^A'.format(name, name2))

print(name + 'さんのBMI値は' + str((weight / (height / 100) ** 2)))
print('%sさんのBMI値は%.1f' % (name, (weight / (height / 100) ** 2)))
print('{}さんのBMI値は{:.1f}'.format(name, weight / (height / 100) ** 2))
print(f'{name}さんのBMI値は{(weight / (height / 100) ** 2):.1f}')

import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
print(locale.getlocale(locale.LC_TIME))

n2 = 123456.789012
print(f"{n2:,}")