import sys

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
    
print(f"平均: {(total / (len(sys.argv) - 1)):.3f}")

print(type(sys.argv))