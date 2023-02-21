list16 = [ 70, 58, 72, 63, 92, 42, 8, 52, 68, 85, 78, 35, 15, 55, 67, 80 ];

counter = {}
for n in range(11):
    counter[n] = 0
    
for score in list16:
    counter[score // 10] += 1

for i in range(10):
    print(f"{i*10:3}-{i*10+9:3}: {counter[i]}")
print(f"100    : {counter[10]}")