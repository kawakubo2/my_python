import os

f = open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='utf_8')
lines = f.readlines()
for i, line in enumerate(lines):
    # print("{:4d}: {}".format(i + 1, line.rstrip('\n')))
    print(f"{i + 1:4d}: {line}", end="")
f.close()