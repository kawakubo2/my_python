count = 0
for i in range(1, 100):
    for j in range(1, 100):
        count += 1
        if i * j > 300:
            break
        print(f"{i*j:2d} ", end="")
    print()
    
print(f'回数: {count}')