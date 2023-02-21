# -*- coding: utf-8 -*-
"""
Created on Sat May  6 22:33:13 2017

@author: tomok
"""

season_en = ['Spring', 'Summer', 'Autumn', 'Winter']
season_ja = ['春', '夏', '秋', '冬']

seasons = {en:ja for en, ja in zip(season_en, season_ja)}
print(seasons)

seasons2 = {ja:en for en, ja in zip(season_en, season_ja)}
print(seasons2)

           