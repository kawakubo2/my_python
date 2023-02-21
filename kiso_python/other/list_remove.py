# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:16:45 2017

@author: tomok
"""

names = ['山田', '井上', '太田', '田中', '山田']
name = '山田'
while name in names:
    names.remove(name)
print(names)
