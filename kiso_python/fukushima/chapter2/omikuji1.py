# -*- coding: utf-8 -*-

import random

kuji = ['大吉', '中吉', '凶']

print(kuji[random.randrange(len(kuji))])

print(random.choice(kuji))

weekdays = '日月火水木金土'

print(random.choice(weekdays))