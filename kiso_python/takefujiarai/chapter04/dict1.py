# -*- coding: utf-8 -*-

colors = {'red': '赤', 'blue': '青', 'yellow': '黄'}

print(colors['blue'])
colors['yellow'] = '黄色'
print(colors)

colors['green'] = '緑'
print(colors)

for en_color, ja_color in colors.items():
    print('{}:{}'.format(en_color, ja_color))
    
seasons = {'春': 'Spring', '夏': 'Summer',
           '秋': 'Autumn', '冬': 'Winter'}

print(seasons)

del seasons['夏']

print(seasons)

try:
    del seasons['晩秋']
except KeyError:
    print('キーが存在しません。')
    
dic = {'日': 'Sun', '月':'Mon', '火': 'Tue','水':'Wed', '木':'Thu', '金': 'Fri', '土':'Sat'}

#key = input('キーを入力してください: ')
#
#if key in dic:
#    del dic[key]
#    print(dic)
#else:
#    print('キー"{}"が見つかりませんでした。'.format(key))

for s in seasons.keys():
    print(s)
    
for s in seasons.values():
    print(s)
    
for ja_season, en_season in seasons.items():
    print("{}:{}".format(ja_season, en_season))
    
for ja_day, en_day in dic.items():
    print("{}:{}".format(ja_day, en_day))
    


