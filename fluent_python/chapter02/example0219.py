import bisect
import random

SIZE = 7

my_list = []

# random.seed(1962)

for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('{:2d} ->'.format(new_item), my_list)