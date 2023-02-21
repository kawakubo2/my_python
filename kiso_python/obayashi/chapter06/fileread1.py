import os

f = open(os.path.dirname(__file__) + "/sample.txt", "r", encoding="UTF-8")
# f = open("sample.txt", "r", encoding="UTF-8")
lines = f.read()
print(lines)
f.close()
