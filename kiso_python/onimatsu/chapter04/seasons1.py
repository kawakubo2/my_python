# -*- coding: utf-8 -*-

seasons = {'春': 'Spring', '夏': 'Summer', '秋': 'Autum', '冬': 'Winter'}

print(seasons.keys())
print(seasons.values())

for ja, en in seasons.items():
    print('{}: {}'.format(ja, en))