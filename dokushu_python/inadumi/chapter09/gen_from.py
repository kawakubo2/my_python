import os

def read_files(*files): 
    for file in files:
        yield from read_lines(file)

def read_lines(path):
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            yield line.rstrip('\n')

base_path = os.path.dirname(__file__)
for line in read_files(
       os.path.join(base_path, 'closure_basic.py'), 
       os.path.join(base_path, 'bubble_sort.py'),
       os.path.join(base_path, 'gen_prime.py')):
    print(line)
