# -*- coding: utf-8 -*-

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekday1, weekday2):
    print(en + ":" + ja)
    
for en, ja in zip(weekday1, weekday2):
    print(ja + ":" + en)
    
    
price = [ 2400, 3000, 1800, 2000 ]
toho  = [ 10, 2, 15, 10]

for p, t in zip(price, toho):
    print("{}万円:徒歩{}分".format(p, t))
    
widths = [ 2, 4, 5, 3, 1]
heights = [ 1, 3, 2, 1, 4]

for w, h in zip(widths, heights):
    print("幅が{}, 高さが{}の長方形の面積は{}です。".format(w, h, w * h))