import os
print(__file__)
base_dir = os.path.dirname(__file__)
f = open(os.path.join(base_dir, "sample.txt"), "r", encoding="utf_8")
lines = f.read()
print(lines)
f.close()