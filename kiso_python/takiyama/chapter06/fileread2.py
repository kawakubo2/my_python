import os

filepath = os.path.join(os.path.dirname(__file__), 'sample.txt')

f = open(filepath, "r", encoding="utf_8")

while True:
    lines = f.read(5)
    if lines == "":
        break
    print(lines)