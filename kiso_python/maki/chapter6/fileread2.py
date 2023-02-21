# -*- coding: utf-8 -*-

f = open("sample.txt", "r", encoding="utf_8")

lines = f.read(10)
print(lines)

lines = f.read(10)
print(lines)

f.close()