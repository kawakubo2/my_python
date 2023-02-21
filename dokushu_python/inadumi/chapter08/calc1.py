total = 0

def add(x):
    global total
    total += x
def sub(x):
    global total
    total -= x
def mul(x):
    global total
    total *= x
def div(x):
    global total
    total /= x
def get_total(): 
    return total