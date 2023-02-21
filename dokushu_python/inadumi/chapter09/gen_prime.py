import math

def gen_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(value):
    result = True
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False
            break
    return result

for prime in gen_primes():
    print(prime)
    if prime > 100:
        break