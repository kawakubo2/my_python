# math1.py
import math

x = 1.0000001000
y = 1.9999999999

print(math.ceil(x))
print(math.floor(x))

index = 0
size = 3
s = "abcdefghijklmnopqrstuvwxyz"
while True:
    temp = s[size * index: size * (index + 1)]
    if temp:
        print(temp)
    else:
        break
    index += 1