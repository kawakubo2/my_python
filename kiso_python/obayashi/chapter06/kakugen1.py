import os, random

f = open(os.path.dirname(__file__) + "/kakugen.txt", "r", encoding="UTF-8")

lines = f.readlines()
kakugen = lines[random.randrange(len(lines))]
print(kakugen.rstrip("\n"))

f.close()
