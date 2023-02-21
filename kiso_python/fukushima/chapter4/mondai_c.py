# -*- coding: utf-8 -*-

langs = {'Python': 45, 'C': 14, 'Swift': 40, 'JavaScript': 40, 'Java': 44}

for l, n in langs.items():
    print("{:10s}の利用者は{}人".format(l, n))
    
from collections import OrderedDict

ja = ['日', '月', '火', '水', '木', '金', '土']
en = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


dict1 = OrderedDict()
for j, e in zip(ja, en):
    dict1[j] = e
    
for j, e in dict1.items():
    print('{}: {}'.format(j, e))