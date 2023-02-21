# -*- coding: utf-8 -*-

str1 = 'javascript is not java'

str2 = 'ja'

cnt = str1.count(str2)

print('"{}"の中に"{}"は{}個あります'.format(str1, str2, cnt))

url = 'https://haru-idea.jp'

if url.startswith('https'):
    print('暗号化通信されています')
else:
    print('暗号化通信されていません')
    
files = ['abc.java', 'bbb.php', 'xxx.py', 'aaa.c', 'yyy.py']

for file in files:
    if file.endswith('.py'):
        print(file)
        
str_files = ','.join(files)

print(str_files)

str3 = 'abacde123fghij123jklm'

str4 = str3.replace('123', '★')

print(str4)

str5 = '123,456,789,012'

str6 = str5.replace(',', '')
print(str6)

str7 = 'Python,Java,PHP,JavaScript,C++,C,Rust'

langs = str7.split(',')
print(langs)

name = '山田太郎'

for c in name:
    print("'{}'の文字コードは{}です".format(c, ord(c)))
    
s = '月火水木金土日'
print(s[::2])
print(s[::-1])