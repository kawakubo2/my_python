import os

filepath = os.path.join(os.path.dirname(__file__), 'out.txt')

with open(filepath, "a", encoding="utf_8") as f:
    f.write("さようなら\n")