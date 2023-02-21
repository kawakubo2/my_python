f = open('sample.txt', 'r', encoding='utf_8')
for i, line in enumerate(f, 1):
    print('{:4d}: {}'.format(i, line.rstrip('\n')))

f.close()
