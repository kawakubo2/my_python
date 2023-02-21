import sys

# sys.argv ---> ["practice_b.py", 1.23, 4.56, 7.89]

if len(sys.argv) < 2:
    print("引数を指定してください")
    sys.exit()

total = 0
for i in range(1, len(sys.argv)):
    total += float(sys.argv[i])
print(f"平均: {total / (len(sys.argv) - 1):.3f}")