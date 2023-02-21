import os

with open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='utf_8') as f:
    for i, line in enumerate(f):
        print("{:4d}: {}".format(i + 1, line.rstrip('\n')))