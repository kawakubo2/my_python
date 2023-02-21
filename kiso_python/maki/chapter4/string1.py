# -*- coding: utf-8 -*-

title1 = 'text analytics with python'
title2 = 'TeXt aNALYTicS WITH PYTHON'

print(title1.upper())
print(title2.lower())
print(title1.title())
print(title1.capitalize())

num = "12345aaa"

if num.isdecimal():
    print(float(num) * 5)
else:
    print('数値のみ入力してください')
    
str1 = '私はJavaを勉強していたが、Pythonの方が面白そうだったので、Pythonに切り替えた'
cnt = str1.count('Python')
print(cnt)

filenames = ['abc.py', 'def.java', 'xyz.c', 'lmn.py']
for file in filenames:
    if file.endswith('.py'):
        print(file)
        
urls = ['http://abc.com', 'https://bbb.jp', 'https://haru-idea.jp']
for url in urls:
    if url.startswith('https'):
        print(url)
        
email = 'tomo.kawakubo@gmail.com'
pos = email.find('@')
print(pos)
if pos >= 0:
    local = email[0:pos]
    domain = email[pos+1:]
    print('ローカル部:', local)
    print('ドメイン部:', domain)
    
langs = ['Python', 'Java', 'Rust', 'Go']
print('@@@'.join(langs))

langs2 = 'Python,Java,PHP,Julia,D,C#'
lang_list = langs2.split(',')
for lang in lang_list:
    print(lang)
print(type(lang_list))

str2 = 'kokohadoko'
print(str2.replace('ko', 'xxx'))

print(len(str2))

str3 = 'Tomoharu Kawakubo'
print(len(str3))
print(len(str3.replace(' ', '')))
