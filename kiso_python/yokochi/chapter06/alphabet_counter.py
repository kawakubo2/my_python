# alphabet_counter.py
import os, time

start = time.time()
counter = {}

A = 65
Z = 90
a = 97
z = 122

# アルファベットをキーとし、値を0で初期化した辞書
for i in range(A, Z+1):
    counter[chr(i)] = 0
for i in range(a, z+1):
    counter[chr(i)] = 0

# for c in counter.keys():
#     print(c)
 
with open(os.path.dirname(__file__) + '/novel.txt', 'r', encoding='utf_8') as f:
    for line in f:
        for c in line:
            if c in counter:
                counter[c] += 1

end = time.time()

print(f"処理時間: {end - start}")
for c, cnt in counter.items():
    print(f"{c}: {cnt}")