from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(f"fibonacci(50)={fibonacci(50)}")
end = time.time()
print(f"処理時間: {end - start}")