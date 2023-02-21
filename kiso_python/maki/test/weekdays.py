# -*- coding: utf-8 -*-

ja_weekdays = ['日','月','火','水','木','金','土']
en_weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for en, ja in zip(ja_weekdays, en_weekdays):
    print('{}:{}'.format(ja, en))
