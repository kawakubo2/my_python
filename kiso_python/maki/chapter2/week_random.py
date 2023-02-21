# -*- coding: utf-8 -*-

import random

weekdays = ['日', '月', '火', '水', '木', '金', '土']

kuji = ['大吉', '中吉', '凶']

janken = ['グー', 'チョキ', 'パー']


def choice(lst):
    return lst[random.randrange(len(lst))]

print(choice(weekdays))

print(choice(kuji))

print(choice(janken))

