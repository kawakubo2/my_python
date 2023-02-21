# -*- coding: utf-8 -*-

name = '山田太郎'

weight = 65
height = 165

def bmi(weight, height):
    return weight / (height / 100) ** 2

print('{1}さんのBMI値は{0:.2f}です。{1}は私の友人です。'.format(bmi(weight, height), name))