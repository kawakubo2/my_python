import sys

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])

print(f"総和: {total}")