# -*- coding: utf-8 -*-

from collections import OrderedDict

ordered_dic1 = OrderedDict()

ordered_dic1['ccc'] = 12345
ordered_dic1['aaa'] = 23456
ordered_dic1['ddd'] = 34567
ordered_dic1['eee'] = 45678
ordered_dic1['bbb'] = 56789

for key, val in ordered_dic1.items():
    print("{}: {}".format(key, val))
    
print('--------------')
    
products = {'c123': 2000, 'a246': 3000, 'c100': 1000,
            'a200': 5000, 'b050': 2500}

for code, price in sorted(products.items(), key=lambda p: p[1]):
    print("{}: {}".format(code, price))
    
ordered_dic2 = OrderedDict()

ja_day_of_weeks = ['日', '月', '火', '水', '木', '金', '土']
en_day_of_weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for ja, en in zip(ja_day_of_weeks, en_day_of_weeks):
    ordered_dic2[ja] = en
    
for ja, en in ordered_dic2.items():
    print(ja + ": " + en)
