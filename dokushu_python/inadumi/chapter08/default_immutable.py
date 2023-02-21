def my_func(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list

print(my_func(13))
print(my_func(108))

def get_triangle(base = 5, height = 1):
    return base * height / 2

print(get_triangle(5, 8))
print(get_triangle(height = 5))
print(get_triangle(height = 8, base = 10))

teihen = 10
takasa = 20

print(get_triangle(teihen, takasa))

print(2021, 6, 6, sep="/", end="")
print('abc')

def div(a, / ,  b):
    return a / b

print(div(20, 4))
print(div(10, b=5))
print(div(10, b=5))

print(1, 2, 'abc', True, [1, 2, 3])

def my_sum(*num):
    total = 0
    for n in num:
        total += n
    return total

print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(my_sum())

numbers = (1, 3, 4, 19, 3, 4, 12)
print(my_sum(*numbers))

print(numbers)
print(*numbers)

name="山田太郎"
age=38
print("{0}さんの年齢は{1}歳です。{0}さんは元気です。".format(name, age))

def fill_in_format(format, *value):
    for i, v in enumerate(value):
        format = format.replace("{" + str(i) + "}", v)
    return format

print(fill_in_format("{0}さんの年齢は{1}歳です。{0}さんは元気です。", name, str(age)))

comingsoon_email = "{0}様\n{1}年{2}月刊行予定の書籍情報です。"

print(fill_in_format(comingsoon_email, "山田太郎", str(2021), str(7)))
print("{0}様\n{1}年{2}月刊行予定の書籍情報です。".format("横山花子", 2021, 7))

# 3 2 7 ---> 3 * 2 * 7
# ---> 1

# 引数を1個以上ほしい時の書き方
def total_product(init, *values):
    result = init
    for v in values:
        result *= v
    return result

print(total_product(3, 2, 7))
print(total_product(10))

def create_dict(**kwargs):
    return kwargs

print(create_dict(name="山田太郎", age=18, sex="male"))
"""
def create_shuffle_list(**kwargs):
    import random
    result = []
    for k, v in kwargs.items():
        result += [k] * v

    random.shuffle(result)
    return result
"""

