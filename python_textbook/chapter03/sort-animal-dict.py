# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 22:01:18 2017

@author: tomoharu
"""

animal_dict = {
        "ライオン": 58,
        "チーター": 110,
        "ラクダ": 60,
        "トナカイ": 80
}

for animal, speed in sorted(animal_dict.items(), key = lambda x: x[1], reverse = True):
    print("{:<5}:{:>4}".format(animal, speed))