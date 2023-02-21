weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekday1, weekday2):
    print('{}: {}'.format(en, ja))

weekday_dic_en = {}
weekday_dic_ja = {}
for en, ja in zip(weekday1, weekday2):
    weekday_dic_en[en] = ja
    weekday_dic_ja[ja] = en
print(weekday_dic_en)
print(weekday_dic_ja)