import os

with open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        print(line, end='')