# -*- coding: utf-8 -*-

f = open('input_file.txt', 'r', encoding='utf_8')

lines = f.read()
print(lines)

f.close()