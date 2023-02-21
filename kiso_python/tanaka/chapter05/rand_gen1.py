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

start = time.time()
gen = random_gen(100000)
for n in gen:
    pass

end = time.time()
print(f"処理時間: {end - start}")