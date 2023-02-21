# -*- coding: utf-8 -*-

names = ['山田','井上','太田','田中','山田']

while '山田' in names:
    names.remove('山田')
    
print(names)

names.insert(0, '山田')
names.append('山田')

print(names)

del names[1]
print(names)

names.insert(1, '井上')
print(names)

del names[1:4]
print(names)



