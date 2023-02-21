numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum1(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(f"sum1(numbers)-->{sum1(numbers)}")

def sum2(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print(f"sum2(numbers)-->{sum2(numbers)}")

def sum3(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(f"sum3(numbers)-->{sum3(numbers)}")

def my_sum(func, nums):
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print(f"正数の和: {my_sum(lambda n: n > 0, numbers)}")
print(f"正数の偶数の和: {my_sum(lambda n: n > 0 and n % 2 == 0, numbers)}")

def positive_even(n):
    return n > 0 and n % 2 == 0

answer = my_sum(positive_even, numbers)
print(answer)

langs = ['Python', 'Java', 'Rust', 'C', 'Go', 'C++', 'JavaScript']

for n in map(lambda s: len(s), langs):
    print(n)

str1 = ['Pythonは機械学習、深層学習でよく使用される', 'JavaやC#は企業の基幹システムとしての利用が多い', 'C言語はハードウェアの制御やミドルウェアで使用される']

for s in map(lambda s: s[:10], str1):
    print(s)