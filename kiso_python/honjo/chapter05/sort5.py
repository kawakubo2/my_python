# -*- coding: utf-8 -*-

names = {'Taro': 55, 'Makoto': 49, 'Akio': 30, 
         'Kazuo': 32, 'Chie': 22, 'Ken': 48}

print('---名前順でsort---')
for name in sorted(names.items(), key=lambda n: n[0]):
    print(name[0], name[1])
    
print('---年齢順でsort---')
#for name in sorted(names.items(), key=lambda n: n[1]):
#    print(name[0], name[1])
    

for name in sorted(names.items(), key=lambda n: n[1]):
    print(name[0], name[1])
    
clazz = ['Platinum', 'Gold', 'Silver', 'Blonde']

members = {'Taro': 'Silver', 'Makoto': 'Gold', 'Akio': 'Platinum',
           'Kazuo': 'Blonde', 'Chie': 'Gold', 'Ken': 'Silver'}

for member in sorted(members.items(), key=lambda n: clazz.index(n[1])):
    print(member[0], member[1])
    
print(members)countries1.py
