# -*- coding: utf-8 -*-
from calendar import TextCalendar, isleap


cal = TextCalendar(firstweekday=6)
cal.pryear(2020)

if (isleap(2020)):
    print('閏年です。')
else:
    print('閏年ではありません。')
    
