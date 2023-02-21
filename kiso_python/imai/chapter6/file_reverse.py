f = open('sample.txt', 'r', encoding='utf_8')
# lines = list(f.readlines())
lines = f.readlines()
lines = lines[:20]
for i, line in enumerate(lines):
    print('{:4d}:{}'.format(i+1, line.rstrip('\n')))