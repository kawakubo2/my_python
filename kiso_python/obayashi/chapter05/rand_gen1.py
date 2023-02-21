import random, time

def random_gen(num):

    randoms = set() 

    while True:
        random_num = random.randrange(num)
        if random_num not in randoms:
            randoms.add(random_num)
            yield random_num
        elif len(randoms) == num:
            break

start=time.time()
for n in random_gen(100000):
    pass
end=time.time()
print(f"処理時間: {end - start}")