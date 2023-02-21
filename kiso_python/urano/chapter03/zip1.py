weekdays1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekdays2 = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekdays1, weekdays2):
    print(en + ':' + ja)