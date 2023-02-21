import os

print(__file__)
print(os.path.join(os.path.dirname(__file__), 'sample.txt'))
filepath = os.path.join(os.path.dirname(__file__), 'sample.txt')
f = open(filepath, "r", encoding="utf_8")
lines = f.readlines()
for line in lines:
    print(line.rstrip("\n"))
f.close()