import random, os

filepath = os.path.join(os.path.dirname(__file__), 'kakugen.txt')

f = open(filepath, "r", encoding="utf_8")
lines = f.readlines()

kakugen = lines[random.randrange(len(lines))]
print(kakugen.rstrip("\n"))