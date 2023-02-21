import random, time

def random_gen(num):
    randoms = set()
    
    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break
num = 1_000_000        
rand = random_gen(num)
start = time.time()
for _ in range(num):
    next(rand)
end = time.time()
print(f"処理時間: {end - start}")