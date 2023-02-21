import os

filepath = os.path.join(os.path.dirname(__file__), 'sample.txt')

f = open(filepath, "r", encoding="utf_8")
lines = f.read(10)
print(lines)
lines = f.read(10)
print(lines)
f.close()