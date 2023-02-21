colors = { 'red': '赤', 'blue': '青', 'yellow': '黄'}

# 値の取得
print(colors['red'])

# 値の上書き
colors['yellow'] = '黄色'
print(colors)

# キーと値の追加
colors['green'] = '緑'
print(colors)

seasons = {'春': 'Spring', '夏': 'Summer', '秋': 'Autumn', '冬': 'Winter'}

# キーと値の削除
del seasons['夏']
print(seasons)


if '晩秋' in seasons:
    del seasons['晩秋']

"""
try:
    del seasons['晩秋']
except KeyError:
    print('晩秋は存在しません')
"""

print(seasons)

colors1 = {"red": "赤", "yellow": "黄色"}
colors2 = {"green": "緑", "blue": "青"}

colors3 = {}
for en_color, ja_color in colors1.items():
    colors3[en_color] = ja_color
for en_color, ja_color in colors2.items():
    colors3[en_color] = ja_color
print(colors3)

seasons = {'春': 'Spring', '夏': 'Summer', '秋': 'Autumn', '冬': 'Winter'}

for s in seasons.keys():
    print(s + ':' + seasons[s])

for v in seasons.values():
    print(v)

for k, v in seasons.items():
    print(k + ':' + v)