list11 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
          "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]

start = 0
step = 5
while True:
    if start + step >= len(list11):
        print(list11[start: len(list11)])
        break;
    print(list11[start: start + step])
    start += step

a = list11[0::3]
b = list11[1::3]
c = list11[2::3]

print(a)
print(b)
print(c)