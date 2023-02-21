# -*- coding: utf-8 -*-

names = {'Taro': 55, 'Makoto': 49, 'Akio': 30, 'Kazuo': 32,
         'Chie': 22, 'Ken': 48}

print('---< キー(名前)でソート >---')
for name in sorted(names.items(), key=lambda n: n[0]):
    print('{:6s}:{}'.format(name[0], name[1]))
    
print('---< 辞書の場合、デフォルトはキーでのソート >---')
for name in sorted(names.items()):
    print('{:6s}:{}'.format(name[0], name[1]))
    
print('---< 値(年齢)でソート >---')
for name in sorted(names.items(), key=lambda n: n[1]):
    print('{:6s}:{}'.format(name[0], name[1]))
    
print('---< 値(年齢)でソート >---')
for name, age in sorted(names.items(), key=lambda n: n[1]):
    print('{:6s}:{}'.format(name, age))