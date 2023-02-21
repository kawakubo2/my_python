seasons = {'春': 'Spring'}
seasons['夏'] = 'Summer'
seasons['秋'] = 'Autumn'
seasons['冬'] = 'Winter'

print(seasons)

del seasons['夏']
print(seasons)

if '晩秋' in seasons:
    del seasons['晩秋']
print(seasons)

colors = {'red': '赤', 'blue': '青', 'yellow': '黄'}
print(colors)

from collections import OrderedDict

colors2 = OrderedDict()

colors2['red'] = '赤'
colors2['blue'] = '青'
colors2['yellow'] = '黄色'
colors2['green'] = '緑'
colors2['white'] = '白'

print(colors2)

for en_color, ja_color in colors2.items():
    print("{}:{}".format(en_color, ja_color))

countries = ['イギリス', 'フランス', 'ドイツ', 'イタリア', 'スペイン']
nums = [6, 9, 3, 14, 8]

answer = []
for country, num in zip(countries, nums):
    answer += [country] * num

import random

random.shuffle(answer)

print(answer)
