# -*- coding: utf-8 -*-

names = ['山田', '井上', '太田', '田中', '山田']

name = '山田'
try:
    while True:
        index = names.index(name)
        del names[index]
except ValueError:
    pass

print(names)

names = ['山田', '井上', '太田', '田中', '山田']
print(names.count(name))
try:
    while True:
        names.remove(name)
except ValueError:
    pass

print(names)

