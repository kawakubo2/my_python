name = input("名前: ")

for c in name:
    print(" {} の文字コードは {}".format(c, ord(c)))

for code_point in range(ord('ァ'), ord('ン') + 1):
    print(chr(code_point))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(numbers[0:5])
print(numbers[5:10])
print(numbers[10:15])
print(numbers[15:20])
