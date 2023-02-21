# -*- coding: utf-8 -*-

f = open("sample.txt", "r", encoding="utf_8")

lines = f.read()
print(lines)

f.close()