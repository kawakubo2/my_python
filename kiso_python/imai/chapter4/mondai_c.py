# -*- coding: utf-8 -*-

langs = {'Python': 45, 'C': 14, 'Swift': 40, 'JavaSript': 40,
        'Java': 44}

for lang, num in langs.items():
    print("{:10}の利用者は{:3}人".format(lang, num))