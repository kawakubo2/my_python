# make_list.py
import random

def make_shuffle_list(dic):
    result = []
    for item, cnt in dic.items():
        result += [item] * cnt
    random.shuffle(result)
    return result