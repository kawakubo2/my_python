def factorial(n):
    if n != 1:
        return n * factorial(n - 1)
    else:
        return 1
    
num = 5

print(f"{num}の階乗は{factorial(num)}")

result = 1
for n in range(1, 6):
    result *= n

print(result)

def my_sum(n):
    if n == 1:
        return n
    else:
        return n + my_sum(n - 1)
    
num = 10
print(f"1から{num}の総和は{my_sum(num)}")