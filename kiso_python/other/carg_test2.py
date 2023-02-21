import sys

sum = 0
for num in range(1, len(sys.argv)):
    sum += float(num)

print("総和: {}".format(sum))
