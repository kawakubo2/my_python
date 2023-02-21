f = open('sample.txt', 'r', encoding="utf_8")

lines = f.readlines()

for i, line in enumerate(lines, start=1):
    print('{:4d}: {}'.format(i, line.rstrip('\n')))