# -*- coding: utf-8 -*-

langs = ['python', 'C', 'Java', 'PHP', 'julia']

# sortedは元のリストには影響を与えず、ソートしたリストを返す
# 大文字小文字を識別してソートする
langs2 = sorted(langs)

print(langs)

print(langs2)

langs3 = sorted(langs, key=str.upper)

print(langs3)

names = ['田中一郎-1979', '山田花子-2000', '井上太郎-1964',
         '藤本和雄-1968', '大津徹-1959', '後藤信-1980']

def get_year(str):
    year = str[-4:]
    return int(year)

names.sort(key=get_year)

print(names)

names = ['田中一郎-1979', '山田花子-2000', '井上太郎-1964',
         '藤本和雄-1968', '大津徹-1959', '後藤信-1980']


names.sort(key=lambda str: int(str[-4:]))

print(names)


names = {'Taro': 55, 'Makoto': 49, 'Akio': 30, 
         'Kazuo': 32, 'Chie': 22, 'Ken': 48 }

print('---< 名前順 >---')
for name in sorted(names.items(), key=lambda n: n[0]):
    print(name[0], name[1])
print('---< 年齢順 >---')  
for name in sorted(names.items(), key=lambda n: n[1]):
    print(name[0], name[1])