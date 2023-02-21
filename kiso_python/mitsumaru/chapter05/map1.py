def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
for cm in map(to_cm, inches):
    print(cm)

def my_map(func, list1):
    for n in list1:
        yield func(n)
print('--- 自作map関数 ---')
for cm in my_map(to_cm, inches):
    print(cm)

for inch in inches:
    print(to_cm(inch))

def sqr(num):
    return num ** 2

for n in map(sqr, inches):
    print(n)

def youbi(y):
    return y + "曜日"

def add(x, y):
    return x + y

for y in map(youbi, "月火水木金土日"):
    print(y)

# map関数は引数が1つ、戻り値がある関数を受け取れる
# for n in map(add, inches):
    print(n)

numbers = [3.23, 81.11, 12.81, 3.44]
def circle(radius):
    import math
    return radius ** 2 * math.pi

for area in map(circle, numbers):
    print(area)