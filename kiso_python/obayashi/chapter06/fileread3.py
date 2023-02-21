import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="UTF-8")

lines = f.readlines()
print(type(lines))
for i, line in enumerate(lines):
    print("{:4d}: {}".format(i+1, line), end="")

f.close()