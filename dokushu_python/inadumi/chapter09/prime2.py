import time

start = time.time()
MAX_NUM = 10_000_000

numbers = [1] * (MAX_NUM + 1)
numbers[0] = 0
numbers[1] = 0

for n in range(2, MAX_NUM + 1):
    if numbers[n] == 1:
        for m in range(n + n, MAX_NUM + 1, n):
            numbers[m] = 0

end = time.time()
print(f"処理時間: {end - start}")

# for n in range(0, MAX_NUM + 1):
#     if numbers[n] == 1:
#         print(n)
# 

