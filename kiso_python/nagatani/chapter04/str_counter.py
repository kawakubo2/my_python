s1 = 'kokohadoko'

s2 = 'ko'
count = s1.count(s2)
if count > 0:
    print(f"{s1}の中に{s2}は{count}個あります。")
else:
    print(f"{s1}の中に{s2}はありません。")
    
suffix = '.py'

filename = 'abc.xyz.py'

if filename.endswith(suffix):
    print('Pythonファイルです。')
else:
    print('Pythonファイルではありません。')

email = 'tomo.kawakubo@gmail.com'

pos = email.find('@')
if pos > -1:
    print(f'ローカル部:{email[:pos]}')
    print(f'ドメイン部:{email[pos+1:]}')

local, domain = email.split('@');
print(f'ローカル部:{local}')
print(f'ドメイン部:{domain}')

lang = ['Python', 'Java', 'C#', 'TypeScript']
s3 = ','.join(lang)
# lang.join(',')
print(s3)

s4 = s1.replace('ko', '') # replaceは非破壊的メソッド
print(s4)
print(s1)

s5 = 'abcdefghijklmnopqrstuvwxyz'
print(s5[::3])
print(s5[-1::-2])
