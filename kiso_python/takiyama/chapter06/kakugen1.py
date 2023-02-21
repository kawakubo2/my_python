import os, random

filepath = os.path.join(os.path.dirname(__file__), 'kakugen.txt')

f = open(filepath, "r", encoding="utf_8")
lines = f.readlines()

kakugen = lines[random.randrange(len(lines))]
print(kakugen)

f.close()