import random
import time

def random_gen(num):
    randoms = set() 

    while True:
        rand_num = random.randrange(num)
        if rand_num not in randoms:
            randoms.add(rand_num)
            yield rand_num
        elif len(randoms) == num:
            break

num = 100000
start = time.time()
for n in random_gen(num):
    pass
    # print("{:2d} ".format(n), end="")
end = time.time()

print("\n{}".format(end-start))