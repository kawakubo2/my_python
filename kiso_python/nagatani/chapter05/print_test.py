import sys

print('a')
print()
print('b')
print('c', 'd', 'e', 123, True)

num = 100
print('num=', num, 'xxx=', 500, 'yyy=', True)
print(1000)

def average(num, *nums):
    total = num
    for n in nums:
        total += n
    return total / (len(nums) + 1)

print(average(100))

upper = lambda s: s.upper()

print(upper('python'))

add = lambda x, y: x + y
a = lambda x: x % 3 == 0
b = lambda x: x > 0 and x % 5 == 0
print(b(25))
print(b(-125))

def myupper(s):
    return s.upper()
def to_cm(inch):
    return inch * 2.54 

numbers = [1, 2, 3, 4, 5, 6, 7]
names = ['Yamada', 'Yokoyama', 'Tanaka']
for n in map(myupper, names):
    print(n)

cms = []
for cm in map(lambda n: n * 2.54, filter(lambda inch: inch > 5, numbers)):
    cms.append(cm)

print(cms)

cms2 = [n * 2.54 for n in numbers if n > 5]
print(cms2)

members = [
    {'name': '山田太郎', 'weight': 60, 'height': 172},
    {'name': '田中一郎', 'weight': 60, 'height': 167},
    {'name': '鈴木次郎', 'weight': 60, 'height': 180},
    {'name': '佐藤勝男', 'weight': 60, 'height': 170},
]

def bmi(weight, height):
    return weight / (height / 100) ** 2

members.sort(key=lambda m: bmi(m['weight'], m['height']), reverse=True)
print(members)