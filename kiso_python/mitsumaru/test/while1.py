import os

f = open(os.path.dirname(__file__) + '/list1.py', 'r', encoding='utf-8')

while True:
    line = f.readline()
    if line == "":
        break
    print(line)

f.close()
