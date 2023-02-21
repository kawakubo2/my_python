# -*- coding: utf-8 -*-

e_seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
j_seasons = ['春', '夏', '秋', '冬']

ej_seasons = {e:j for e,j in zip(e_seasons, j_seasons)}
print(ej_seasons)
je_seasons = {j:e for e,j in zip(e_seasons, j_seasons)}
print(je_seasons)

seasons1 = {'Summer': '夏', 'Autumn': '秋', 'Winter': '冬', 'Spring': '春'}
seasons2 = {j:e for e,j in seasons1.items()}
print(seasons2)

lst = [100, 200, 100, 200, 300, 300, 400, 90, 100, 400, 50]

num = {num for num in lst if num > 100}
print(num)

tpl = tuple(lst)
print(tpl)