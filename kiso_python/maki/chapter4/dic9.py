# -*- coding: utf-8 -*-

seasons = {'春': 'Spring', '夏': 'Summer', '秋': 'Autumn', '冬': 'Winter'}

for ja_season in seasons.keys():
    print(ja_season + ':' + seasons[ja_season])
    
for ja_season, en_season in seasons.items():
    print(ja_season + ':' + en_season)
    