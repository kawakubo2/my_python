import time

start_time = time.perf_counter()
total = 0
MAX = 100_000_000
for n in range(317, MAX + 1, 317):
    total += n
end_time = time.perf_counter()
    
print(f"1～1億までに存在する317の倍数の合計: {total}")
print(f"処理時間: {end_time - start_time}")