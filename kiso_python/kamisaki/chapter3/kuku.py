count = 0
for i in range(1, 10):
    for j in range(1, 10):
        count += 1 # count = count + 1
        if i * j > 30:
            break
        print("{:2} ".format(i * j), end='')
    print()

print(f"回数: {count}")
"""
n += 10 ---> n = n + 10
n -= 8  ---> n = n - 8
n *= 3  ---> n = n * 3
n /= 2  ---> n = n / 2 
"""