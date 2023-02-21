import math, time

MAX_NUM = 10_000_000
start = time.time()
numbers = []
def gen_primes(max):
    num = 2
    while True:
        if num > max: break
        if is_prime(num):
            numbers.append(num)
        num += 1

def is_prime(value):
    result = True
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result

gen_primes(MAX_NUM)

end = time.time()
print(f"処理時間: {end - start}")
# for n in numbers:
#     print(n)