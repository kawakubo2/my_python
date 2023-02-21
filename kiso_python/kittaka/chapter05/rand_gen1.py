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

num = 100_000

start = time.time()
rg = random_gen(num)
for n in rg:
    pass
end = time.time()
print(f"処理時間: {end - start}")
#for r in rg:
#    print(r)