import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="UTF-8")
lines = f.read(2)
print(lines)
lines = f.read(2)
print(lines)
f.close()
