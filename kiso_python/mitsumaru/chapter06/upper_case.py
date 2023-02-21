import os

f = open(os.path.dirname(__file__) + '/linenum2.py')

while True:
    line = f.readline()
    if line == '':
        break
    print(line.rstrip('\n').upper())