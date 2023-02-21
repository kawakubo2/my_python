def factorial(num):
    if num > 0:
        return num * factorial(num - 1)
    return 1

n = 30
print(f"{n}の階乗は{factorial(n)}")