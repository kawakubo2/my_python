import sys

sum = 0
for n in range(1, len(sys.argv)):
    sum += float(sys.argv[n])

print("平均: {:.3f}".format(sum / (len(sys.argv) - 1)))
