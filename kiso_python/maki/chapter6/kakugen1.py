# -*- coding: utf-8 -*-

import random

f = open("kakugen.txt","r", encoding="utf_8")

lines = f.readlines()
print(type(lines))

kakugen = lines[random.randrange(len(lines))]
print(kakugen.rstrip("\n"))

f.close()