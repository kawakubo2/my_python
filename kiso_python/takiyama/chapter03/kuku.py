counter = 0
for i in range(1, 100):
    for j in range(1, 100):
        counter += 1
        if i * j > 300:
            break
        print(f"{i:2}*{j:2}={i*j:3} ", end="")
    print()
    
print(f"回数: {counter}")