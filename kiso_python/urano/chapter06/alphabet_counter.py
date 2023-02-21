# alphabet_counter.py
import os, time

start = time.time()
counter = {}

with open(os.path.dirname(__file__) + '/novel.txt', 'r', encoding='utf_8') as f:
    for line in f:
        for c in line:
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1

end = time.time()

print(f"処理時間: {end - start}")
for c, cnt in sorted(counter.items()):
    print(f"{c}: {cnt:6d}")

