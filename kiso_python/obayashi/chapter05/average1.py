def average(*nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

print(average())
print(average(10))
print(average(1, 2, 3, 4, 5, 6))

def rectangle(width, height):
    return width * height

print(rectangle(8, 5))
print(rectangle(height=12, width=8))

def func3(**dic):
    print(dic)

func3(name="山田太郎", age=28, height=170, weight=72)