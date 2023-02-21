# distance.py
import math

p1 = (3, 6)
p2 = (6, 10)

distance = math.hypot(p1[0] - p2[0], p1[1] - p2[1]) 

print(f'点({p1[0]},{p1[1]}), 点({p2[0]},{p2[1]})の距離は{distance:.3f}です。')

def my_floor(num, keta):
    num *= math.pow(10, keta)
    num = math.floor(num)
    return num / math.pow(10, keta)

def my_floor2(num, keta):
    return math.floor(num * math.pow(10, keta)) / math.pow(10, keta)

x = 12.34567
print(my_floor2(x, 2))
y = 1234567.89
print(my_floor2(y, -3))