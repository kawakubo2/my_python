# -*- coding: utf-8 -*-

e_seasons = ['spring', 'summer', 'autumn', 'winter']
j_seasons = ['春', '夏', '秋', '冬']

ej_seasons = {e.upper():j for e,j in zip(e_seasons, j_seasons)}
print(ej_seasons)

je_seasons = {j:e.capitalize() for e,j in zip(e_seasons, j_seasons)}
print(je_seasons)