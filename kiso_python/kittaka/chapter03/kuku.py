counter = 0
for i in range(1, 100):
    for j in range(1, 100):
        counter += 1
        if i * j > 300:
            break
        print(f"{i * j:5}", end="")
    print()
    
print(f"counter={counter}")