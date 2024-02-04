x = 0.2
y = 0.6

"""
x * 3 == y ---> True
"""

print(x * 10 * 3 == y * 10)

def equals(x, y):
    import math
    EPSILON = 10 ** -15
    return math.fabs(x - y) < EPSILON

print(equals(x * 3, y))