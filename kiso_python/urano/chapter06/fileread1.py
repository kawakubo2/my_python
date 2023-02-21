# fileread1.py

import os

f = open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='utf_8')
lines = f.read()
print(lines)
f.close()