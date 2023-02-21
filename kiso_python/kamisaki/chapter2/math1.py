from math import ceil, floor, pow, pi

x = 1.000001
y = 1.999999

print(ceil(x))
print(floor(x))

print(ceil(y))
print(floor(y))

my_power = 1

my_power = my_power * pow(1.01, 365)
print('1年後の私: {}'.format(my_power))
    
radius = 5
print(f"半径{radius}cmの円の面積は{pow(radius, 2)*pi:.1f}平方cmです。")