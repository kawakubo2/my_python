total = 0

for n in range(1, 101):
    total += n
    if total > 1000:
        break
    
print(f"1000を超えるのは{n}")

total = 0
for n in range(45):
    total += n
    
print(total)
    