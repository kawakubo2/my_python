# -*- coding: utf-8 -*-

weekday1 = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
weekday2 = ['日', '月', '火', '水', '木', '金', '土']

for en, ja in zip(weekday1, weekday2):
    print(ja + ': ' + en)
    
    
upperbases = [1, 2, 3, 4, 5]
lowerbases = [2, 3, 4, 5, 6]
heights    = [3, 4, 5, 6, 7]

for u, l, h in zip(upperbases, lowerbases, heights):
    print('上底が{}cm、下底が{}cm、高さが{}cmの台形の面積は{}平方cmです'.format(\
          u, l, h, (u + l) * h))