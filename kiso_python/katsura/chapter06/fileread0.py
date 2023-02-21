import os

f = open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='utf_8')
while True:
    s = f.read(5)
    if s == '':
        break
    print(s)

f.close()
        