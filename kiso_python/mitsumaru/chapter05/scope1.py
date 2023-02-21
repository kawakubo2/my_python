value1 = 1

def scope_test1():
    print(value1)

scope_test1()

def scope_test2():
    value2 = 1

# print(value2)

value3 = 1
def scope_test3():
    global value3
    value3 = 100
    print("内部: ", value3)

scope_test3()
print("外部: ", value3)

print('abc', 123, 'あいう', True, False)
print()

def func(arg1, *arg2):
    print(arg1, arg2)

func(1, 2, 3, 4)
func("hello", "Python", 2015, 3, 5)

def student_score(name, *score):
    print(name, end="")
    total = 0
    for s in score:
        total += s
        print(f"{s} ", end="")
    print("合計:", total)

student_score("山田太郎", 70, 58, 62, 88, 100)
student_score("田中一郎", 90, 82, 85, 96)
student_score("鈴木次郎")

def calc_rectangle(width, height):
    return width * height

w = 10
h = 5
print(calc_rectangle(w, h))
print(calc_rectangle(height = 12, width = 6))

def average(*nums):
    if len(nums) == 0:
        return 0
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

print(average(1, 10, 100))
print(average())

# print(sum(1, 2, 3, 4))
print(sum([1, 2, 3, 4]))
print(sum((1, 2, 3, 4)))

age = 19 

if age >= 20:
    print('お酒の販売は可能です')
    print('煙草も吸えます')

