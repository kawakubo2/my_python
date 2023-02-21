def func(**dic):
    print(dic)

func(name="田中一郎", num=1)
func(name="山田太郎", age=59, num=2, point=60)

def circle_area(radius):
    import math

    return radius ** 2 * math.pi

circle = circle_area

print(circle(5))

trapezoid = lambda upperbase, lowerbase, height: (upperbase + lowerbase) * height / 2

print(trapezoid(4, 6, 5))

smaller = lambda num1, num2: num2 if num1 > num2 else num1

print(smaller(5, 19))
print(smaller(-19, -28))

# 高階関数・・・関数の引数として関数を受け取る、もしくは関数を返す関数の事
def func1(list1):
    import random
    r = random.randrange(2)
    if r == 0:
        return lambda : [n for n in list1 if n % 2 ==  0]
    else:
        return lambda : [n for n in list1 if n % 2 !=  0]


my_filter = func1([1, 2, 3, 4, 5, 6])

print(my_filter())
import math
print(math.floor(1.9999999))
print(math.ceil(1.0000001))

def my_floor(num, keta):
    return math.floor(num * (10 ** keta)) / 10 ** keta
def my_ceil(num, keta):
    return math.ceil(num * (10 ** keta)) / 10 ** keta

print(my_floor(1.234567, 3))
print(my_ceil(1.234567, 3))

def my_round(func, num, keta):
    return func(num * (10 ** keta)) / 10 ** keta

print(my_round(math.floor, 1.234567, 3))
print(my_round(math.ceil, 1.234567, 3))