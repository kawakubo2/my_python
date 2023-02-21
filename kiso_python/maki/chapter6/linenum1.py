# -*- coding: utf-8 -*-

f = open("sample.txt", "r", encoding="utf_8")

lines = f.readlines()

for i, line in enumerate(lines):
    print("{:4d} {}".format(i + 1, line.rstrip("\n")))