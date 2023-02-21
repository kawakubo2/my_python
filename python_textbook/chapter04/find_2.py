# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:57:34 2017

@author: tomok
"""

with open("mt7_7.txt", encoding="utf-8") as tf:
    for i, line in enumerate(tf):
        print("{:>3}:{}".format(i+1, line), end="")
