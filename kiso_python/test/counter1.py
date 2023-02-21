# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:08:53 2020

@author: tomok
"""

from collections import Counter
import requests

str1 = "jglajgkegjjjeljkaahejjflejlncbbbavvei"

cnt = Counter(str1)

for c, num in cnt.items():
    print('{}: {}'.format(c, num))
    
res = requests.request('get', 'https://haru-idea.jp')
print(res.text)