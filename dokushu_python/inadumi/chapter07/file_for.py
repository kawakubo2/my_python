import os

with open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='UTF-8') as file:
    file.seek(6)
    for line in file:
        print(line, end='')