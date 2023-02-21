list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
i = 0
size = 3
while True:
    temp = list1[size * i: size * (i + 1)]
    if temp == []:
        break
    print(temp)
    i += 1

email = 'tomo.kawakubo@gmail.com'
pos = email.find('@')
print(email[:pos])