# -*- coding: utf-8 -*-

letter_A = []

for i in range(6):
    temp = []
    for j in range(6):
        temp.append(int(input('letter_A[' + str(i) + '][' + str(j) + ']=')))
    letter_A.append(temp)

print(letter_A)
        