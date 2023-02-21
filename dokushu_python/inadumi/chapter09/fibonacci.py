import time
from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

n = 300
start = time.time()
result = fibonacci(n)
end = time.time()
print(f"fibonacchi({n}): {result}")
print(f"処理時間: {end - start}")