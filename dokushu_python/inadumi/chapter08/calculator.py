total = 0

def add(x):
    global total
    total += x

def sub(x):
    global total
    total -= x # total = total + x

def mul(x):
    global total
    total *= x

def div(x):
    global total
    total /= x

add(100)
print(total)
sub(50)
print(total)
mul(4)
print(total)
div(100)
print(total)