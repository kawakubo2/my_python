import os

with open(os.path.dirname(__file__) + '/access.log', 'r', encoding='UTF-8') as file:
    data = file.readlines()

for line in data[::-1]:
    print(line.rstrip("\n"))
