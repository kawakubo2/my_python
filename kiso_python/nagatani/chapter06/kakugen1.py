import os, random

f = open(os.path.dirname(__file__) + '/kakugen.txt', 'r', encoding='utf_8')
lines = f.readlines()
# kakugen = lines[random.randrange(len(lines))]
kakugen = random.choice(lines)
print(kakugen.rstrip("\n")) 

f.close()