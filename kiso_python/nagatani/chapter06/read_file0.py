import os, sys

print(f"__file__={__file__}")
f = open(os.path.dirname(__file__) + '/sample.txt', encoding='utf_8')
lines = f.read(1)
while lines:
    print(lines)
    lines = f.read(1)
f.close()
