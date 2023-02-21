# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:16:21 2021

@author: tomok
"""

from calendar import TextCalendar

year = int(input('年を入力してください: '))
month = int(input('月を入力してください: '))

cal = TextCalendar(6)

cal.prmonth(year, month)