import os

f = open(os.path.dirname(__file__) + '/kokoro.txt', 'r', encoding='utf-8')
lines = f.readlines()

for i, line in enumerate(lines[::-1]):
    print("{:4d}: {}".format(i + 1, line.rstrip("\n")))