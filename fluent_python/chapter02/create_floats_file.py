import random

ROWS = 10000000

with open('floats-10M-lines.txt', 'w') as f:
    for i in range(ROWS):
        f.write(str(random.random()))
        f.write("\n")
