import os

f = open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='utf_8')
while True:
    line = f.read(3)
    if line == '':
        break
    print(line)

f.close()