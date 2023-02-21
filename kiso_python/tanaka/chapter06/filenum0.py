import os
import list_util

filepath = os.path.join(os.path.dirname(__file__), 'sample2.txt')
f = open(filepath, 'r', encoding='utf_8')
lines = f.readlines()

print(list_util.slice_list(lines, 1, 3))

lines.reverse()
for line in lines:
    print(line.rstrip("\n"))
    
f.close()