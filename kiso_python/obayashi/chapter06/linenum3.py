import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="UTF-8")

for i, line in enumerate(f):
    print("{:4d}: {}".format(i+1, line.rstrip("\n")))

f.close()