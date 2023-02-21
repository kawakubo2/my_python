from collections import defaultdict

en_week = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水', 'Thu': '木', 'Fri': '金', 'Sat': '土'}

ja_week = {value: key for key, value in en_week.items()}

print(ja_week)

dic1 = defaultdict(list)

data = ['apple', 'orange', 'melon', 'pear', 'olive', 'apricot', 'mango']

for f in data:
    dic1[f[0]] += [f]

print(dic1)

