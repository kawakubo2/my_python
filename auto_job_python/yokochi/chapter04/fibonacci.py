def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

num = 10

print(f"フィボナッチ数{num}は{fibonacci(num)}")

def fibonacci2(n):
    if n in (0, 1):
        return n
    num1 = 0
    num2 = 1
    
    for i in range(2, n+1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num3

print(f"フィボナッチ数{num}は{fibonacci(num)}")
        
            