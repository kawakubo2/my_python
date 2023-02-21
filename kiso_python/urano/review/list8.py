list8 = ['X', 'L', 'A', 'B', 'X', 'L', 'C', 'X', 'A', 'B', 'X', 'Y', 'C', 'A']

counter = {}

for c in list8:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1
        
for c, count in counter.items():
    print(f"{c}: {count}")
        
