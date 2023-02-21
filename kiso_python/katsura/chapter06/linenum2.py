import os

f = open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='utf_8')

i = 0
while True:
    line = f.readline()
    if line == '':
        break
    print('{:4d}: {}'.format(i+1, line.rstrip('\n')))
    i += 1 

f.close()