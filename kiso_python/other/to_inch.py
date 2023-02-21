# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:51:07 2017

@author: tomok
"""

cm = float(input('センチメートルを入力してください: '))
print("{:,.3f}cmは{:,.3f}インチです".format(cm, cm / 2.54))