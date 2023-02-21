f = open('kakugen.txt', 'r', encoding='utf_8')

for line in f:
    print(line.rstrip('\n'))

f.close()