# -*- coding: utf-8 -*-

dic = {'日':'Sun', '月':'Mon', '火':'Tue',
       '水':'Wed', '木':'Thu', '金':'Fri', '土':'Sat'}

key = input('キーを入力してください: ')
if key in dic:
    del dic[key]
    print(dic)
else:
    print('キー"{}"が見つかりませんでした。'.format(key))
    
from collections import OrderedDict

ordered_dic = OrderedDict()
ordered_dic['春'] = 'Spring'
ordered_dic['夏'] = 'Summer'
ordered_dic['秋'] = 'Autumn'
ordered_dic['冬'] = 'Winter'

for ja_season in ordered_dic:
    print(ja_season + ':' + ordered_dic[ja_season])
    

