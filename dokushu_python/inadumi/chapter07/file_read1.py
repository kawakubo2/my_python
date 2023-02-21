import os

with open(os.path.dirname(__file__) + '/sample.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
print(data)
print(type(data))