# alphabet_counter.py
import os, time

start = time.time()
counter = {}
with open(os.path.dirname(__file__) + '/The_Return_of_the_Native_pg122.txt', 'r', encoding='utf_8') as f:
    for line in f:
        for c in line:
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1
                    
for char, count in sorted(counter.items()):
    pass
    # print(f'{char}: {count: 6d}')

end = time.time()

print(f'処理時間: {end - start}ms')