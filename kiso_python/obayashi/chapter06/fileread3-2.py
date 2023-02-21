import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="UTF-8")

s = f.read()
lines = s.rstrip("\n").split("\n")
for num, line in enumerate(lines):
    print("{:4d}: {}".format(num+1, line))

f.close()