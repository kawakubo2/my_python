import os, time

filepath = os.path.join(os.path.dirname(__file__), 'The_Return_of_the_Native_pg122.txt')

start = time.time()

Anum = ord('A')
Znum = ord('Z')
anum = ord('a')
znum = ord('z')

counter = {}
for i in range(Anum, Znum + 1):
    counter[chr(i)] = 0
for i in range(anum, znum + 1):
    counter[chr(i)] = 0

with open(filepath, "r", encoding="utf_8") as f:
    for line in f:
        for c in line:
            if c in counter:
                counter[c] += 1

end = time.time()
                
for c, num in counter.items():
    print(f"{c}: {num}")

print(f"処理時間: {end - start}")