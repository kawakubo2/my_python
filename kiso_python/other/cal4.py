# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:37:53 2017

@author: tomok
"""

from calendar import TextCalendar

year = int(input("年を入力してください: "))
month = int(input("月を入力してください: "))

cal = TextCalendar(6)
cal.prmonth(year, month)
