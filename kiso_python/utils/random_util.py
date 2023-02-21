import random

def make_random_list(dic):
    result = []
    for key, count in dic.items():
        result += [key] * count
    random.shuffle(result)
    return result