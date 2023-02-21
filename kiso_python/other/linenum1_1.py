f = open('rand_gen1.py', 'r', encoding='utf_8')

lines = f.readlines()

for line in lines:
    print(line.rstrip("\n"))

