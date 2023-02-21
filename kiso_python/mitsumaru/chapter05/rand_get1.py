import random
import time

def rand_gen(num):
    randoms = set()

    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break

start = time.time()
rand = rand_gen(10)
for n in rand:
    print(n)

end = time.time()
print(f"処理時間: {end - start}")