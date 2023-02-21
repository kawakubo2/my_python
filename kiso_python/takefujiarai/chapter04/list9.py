# -*- coding: utf-8 -*-

season = ['春', '夏']

season += ['秋']
season += ['冬', '真冬']

print(season)

season.append('晩秋')
season.append('初夏')

print(season)

lang = ['Python', 'Java', 'Go', 'Julia', 'Scala', 'C']

print(lang[:lang.index('Julia')])

lang2 = lang[::-1]
#lang2[0] = 'JavaScript'
#print(lang[0])
print(lang2)
print(lang[:5])

print(','.join(lang))
str = ','.join(lang)

lang3 = str.split(',')
print(lang3)
