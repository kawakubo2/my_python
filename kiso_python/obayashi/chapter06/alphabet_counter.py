import os, time

start = time.time()
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets += alphabets.lower()

counter = {c: 0 for c in alphabets}

with open(os.path.dirname(__file__) + "/The_Return_of_the_Native_pg122.txt", "r", encoding="UTF-8") as f:
    for line in f:
        for c in line:
            if c in counter:
                counter[c] += 1

end = time.time()

for c, num in counter.items():
    print(f"{c}: {num:6d}")

print(f"処理時間: {end - start}")