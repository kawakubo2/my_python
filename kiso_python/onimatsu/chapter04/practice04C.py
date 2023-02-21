# -*- coding: utf-8 -*-

langs = {'Python': 45, 'C': 14, 'Swift': 40, 'JavaScript': 40, 'Java': 44}

for lang, num in langs.items():
    print('{:10s}の利用者は{}人'.format(lang, num))