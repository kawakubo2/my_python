import os

filepath = os.path.join(os.path.dirname(__file__), 'sample.txt')

with open(filepath, "r", encoding="utf_8") as f:
    for i, line in enumerate(f):
        print("{:4d}: {}".format(i + 1, line.rstrip("\n")))
