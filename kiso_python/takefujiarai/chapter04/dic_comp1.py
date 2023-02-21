# -*- coding: utf-8 -*-

colors = ['yellow', 'pink', 'blue', 'green']

colors_dic = {color:1 for color in colors}
print(colors_dic)

e_seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
j_seasons = ['春', '夏', '秋', '冬']

ej_seasons = {e:j for e,j in zip(e_seasons, j_seasons)}
print(ej_seasons)

je_seasons = {j:e for e,j in zip(e_seasons, j_seasons)}
print(je_seasons)