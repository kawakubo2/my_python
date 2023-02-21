import random

def make_random_list(dic):
    result = []
    for elem, num in dic.items():
        result += [elem] * num
    random.shuffle(result)
    return result
