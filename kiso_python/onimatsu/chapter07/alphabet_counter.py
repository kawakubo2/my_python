import os, time

start = time.time()

counter = {}

sl = "abcdefghijklmnopqrstuvwxyz"
su = sl.upper()
s = su + sl
for c in s:
    counter[c] = 0 # { 'A': 0, 'B': 0, ・・・ , 'Z': 0, 'a': 0, 'b': 0, ・・・, 'z': 0}

with open(os.path.dirname(__file__) + "/The_Return_of_the_Native_pg122.txt", "r", encoding="utf_8") as f:
    for line in f:
        for c in line:
            if c in counter:
                counter[c] += 1

for c, count in counter.items():
    print(f"{c}: {count:5d}")

end = time.time()

print(f"処理時間: {end - start}")