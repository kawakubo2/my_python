from time import time, sleep
from datetime import datetime

def time_deco(func):
    def inner(*args, **keywords):
        print(f'{func.__name__} Start: {datetime.fromtimestamp(time())}')
        result = func(*args, **keywords)
        print(f'{func.__name__} End: {datetime.fromtimestamp(time())}')
        return result
    return inner

@time_deco
def hoge():
    sleep(3)
    print('hoge is running')

hoge()

@time_deco
def print_number(num):
    for n in range(num + 1):
        if n % 10000000 == 0:
            print(n)

print_number(100000000)