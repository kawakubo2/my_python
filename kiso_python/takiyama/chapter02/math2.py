from math import ceil, floor, pow

x = 1.23456
x *= pow(10, 3)
x = ceil(x)
x /= pow(10, 3)
print(x)

def myceil(num, prec):
    import math
    num *= math.pow(10, prec)
    num = math.ceil(num)
    return num / math.pow(10, prec) 

y = 3289.418974
print(myceil(y, 2))
