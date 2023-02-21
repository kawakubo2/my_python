# -*- coding: utf-8 -*-

langs = {'Python': 45, 'C': 14, 'Swift': 40, 
        'JavaScript': 40, 'Java': 44}

print('---< itemsメソッドを使用 >---')
for lang, num in langs.items():
    print('{}の利用者は{}人'.format(lang, num))

print('---< keysメソッドを使用 >---')
for lang in langs.keys():
    print('{}の利用者は{}'.format(lang, langs[lang]))