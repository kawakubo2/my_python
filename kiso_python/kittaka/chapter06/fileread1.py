import os

filepath = os.path.join(os.path.dirname(__file__), 'sample.txt');
f = open(filepath, "r", encoding="utf_8")

lines = f.read()
print(lines)
f.close()