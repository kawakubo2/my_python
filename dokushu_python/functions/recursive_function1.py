def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 5
print('{}の階乗は{}'.format(num, factorial(num)))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

num = 21
print('{}のフィボナッチ数は{}'.format(num, fibonacci(num)))

numbers = [1, [2, 3, [4, 5, [6, 7]], [8, 9], 10]]

def my_array_sum(nums):
    total = 0
    for n in nums:
        if type(n) == int:
            total += n
        else:
            total += my_array_sum(n)
    return total

print(my_array_sum(numbers))