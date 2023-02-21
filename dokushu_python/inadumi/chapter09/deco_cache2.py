from functools import lru_cache
import time, random

@lru_cache
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

start = time.time()
for n in range(100000):
    fib(random.randrange(20))

end = time.time()
print(f"処理時間: {end - start}")