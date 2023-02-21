import os, time

start = time.time()

counter = {}

f = open(os.path.dirname(__file__) + '/abc.txt', 'r', encoding='utf_8')
while True:
    line = f.read()
    if line == "":
        break
    for c in line:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

end = time.time()

print(f"処理時間: {end - start}")

for char, count in sorted(counter.items()):
    print(f"{char}: {count:6}")

f.close()
