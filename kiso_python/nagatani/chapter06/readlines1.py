import os

f = open(os.path.dirname(__file__) + '/abc.txt', 'r', encoding='utf_8')

i = 0
while True:
    line = f.readline()
    if line == '':
        break
    print("{:6d}: {}".format(i + 1, line.rstrip("\n")))
    i += 1