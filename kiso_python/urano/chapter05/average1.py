def average(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)

print(average(1, 10, 100))
print(average(5, 12, 128, 38, 37, 18, 87, 55, 103, 98, 7))

def max_length(*langs):
    max = 0
    for lang in langs:
        if len(lang) > max:
            max = len(lang)
    return max

print(max_length("PHP", "C", "Python", "C++", "Swift", "JavaScript", "Go", "Rust"))

def mymax(*nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def mymin(*nums):
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    return min
    
def mysum(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

print(mymax(110, 77, 90, 72, 139, 55, 68, 60, 128, 107))
print(mymin(110, 77, 90, 72, 139, 55, 68, 60, 128, 107))
print(mysum(110, 77, 90, 72, 139, 55, 68, 60, 128, 107))

def printchar(c, num):
    print(c * num, end='')

def pyramid(dansu):
    for i in range(1, dansu + 1):
        printchar(' ', dansu - i)
        printchar('*', i * 2 - 1)
        printchar(' ', dansu - i)
        print()

pyramid(10)

def calc_price(weight, size):
    if weight <= 2:
        if size <= 100:
            price = 500
        elif size <= 300:
            price = 1000
        else:
            price = 2000
    elif weight <= 5:
        if size <= 100:
            price = 700
        elif size <= 300:
            price = 1200
        else:
            price = 2200
    else:
        if size <= 100:
            price = 1000
        elif size <= 300:
            price = 1500
        else:
            price = 3000
    return price

w = 4.5
s = 360
print(f"重さが{w}kg、サイズが{s}cmの配送料金は{calc_price(w, s)}円となります。")

"""
10 + 11 + 12 + ... + 20
"""
def sum_range(start, end):
    sum = 0
    for n in range(start, end + 1):
        sum += n
    return sum

print(sum_range(10, 20))
print(sum_range(1, 10))

"""
bmi = 体重(kg) / (身長(m) * 身長(m))
"""
def bmi(weight, height):
    return weight / (height / 100) ** 2

w = 88
h = 180
print(f"体重が{w}kg、身長が{h}cmの人のBMI値は{bmi(w, h):.1f}です。")

members = [
    ('山田太郎', 68, 170),
    ('田中一郎', 82, 178),
    ('鈴木次郎', 80, 180),
    ('佐藤勝男', 60, 160)
]

for member in members:
    print(f"{member}:bmi->{bmi(member[1], member[2])}")

def max_bmi(members):
    max = bmi(members[0][1], members[0][2])
    max_member = members[0]
    for member in members:
        if bmi(member[1], member[2]) > max:
            max = bmi(member[1], member[2])
            max_member = member
    return max_member

def min_bmi(members):
    min = bmi(members[0][1], members[0][2])
    min_member = members[0] 
    for member in members:
        if bmi(member[1], member[2]) < min:
            min = bmi(member[1], member[2])
            min_member = member
    return min_member

fat_man = max_bmi(members)
print(fat_man)

skinny_man = min_bmi(members)
print(skinny_man)
