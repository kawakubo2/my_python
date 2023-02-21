# -*- coding: utf-8 -*-

from collections import OrderedDict

e_seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
j_seasons = ['春', '夏', '秋', '冬']

seasons = {e:j for e, j in zip(e_seasons, j_seasons)}

print(seasons)

seasons2 = OrderedDict()

for e, j in zip(e_seasons, j_seasons):
    seasons2[e] = j
    
print(seasons2)