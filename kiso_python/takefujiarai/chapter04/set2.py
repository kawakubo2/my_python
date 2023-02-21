# -*- coding: utf-8 -*-

fridge = {'ジャガイモ', 'ニンジン', 'タマネギ', 'ブタニク'}

recipes = [
        {'ジャガイモ', 'ニンジン', 'サンマ', 'タマゴ'},
        {'ブタニク', 'タマネギ', 'ジャガイモ'},
        {'ギュウニュウ', 'チーズ', 'コムギコ'},
]

for recipe in recipes:
    # print(recipe)
    if recipe.issubset(fridge):
        print(recipe)