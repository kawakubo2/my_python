import time

MAX = 100_000_000

start_time = time.perf_counter()
total = 0
for n in range(317, MAX, 317):
    total += n
end_time = time.perf_counter()
print(total)
print(f"処理時間: {end_time - start_time}")