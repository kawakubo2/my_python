# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:00:38 2017

@author: tomok
"""

from calendar import TextCalendar

cal = TextCalendar(6)
cal.prmonth(1962, 8)
cal.prmonth(2038, 1)
cal.prmonth(2038, 2)