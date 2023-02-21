# -*- coding: utf-8 -*-

colors = {'red': '赤', 'blue': '青', 'yellow': '黄'}

# 要素数を求める
print(len(colors))

# 値を取り出す
print(colors['red'])

# 値を更新する
colors['yellow'] = '黄色'
print(colors)

# キーと値のペアを削除する
seasons = {'春': 'Spring', '夏': 'Summer', '秋': 'Autum', '冬': 'Winter'}

del seasons['夏']
print(seasons)

season = '晩秋'
if season in seasons:
    del seasons[season]
else:
    print(season + 'は存在しません')