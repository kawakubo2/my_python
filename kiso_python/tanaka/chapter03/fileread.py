import os

f = open(os.path.dirname(__file__) + '/if3.py', 'r', encoding='utf_8')

line = f.readline()
while line != '':
    print(line, end='')
    line = f.readline()
    
f.close()