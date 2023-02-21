# -*- coding: utf-8 -*-

d2 = [
    [7, 7, 7, 7],
    [7, 7, 7, 7],
    [7, 7, 7, 7],
    [7, 7, 7, 7]
]

result = []
for i in range(5):
    sub = []
    for j in range(4):
        sub.append(7)
    result.append(sub)
    
print(result)

print('----------------------------------')

result2 = [[7 for j in range(4)] for i in range(5)]

print(result2)


letter_A = [
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
]

for row in letter_A:
    for bit in row:
        if bit == 1:
            print('@', end='')
        else:
            print(' ', end='')
    print('')
    
for row in letter_A:
    for bit in row:       
        print('@' if bit == 1 else ' ', end='')
    print('')
    
letters = [
    [
        [0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0]
    ],
    [
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0]
    ]
]

for i in range(len(letters)):
    for j in range(len(letters[i])):
        for k in range(len(letters[i][j])):
            if letters[i][j][k] == 1:
                print('@', end='')
            else:
                print(' ', end='')
        print('')
    print('')
    
for matrix in letters:
    for row in matrix:
        for bit in row:
            if bit == 1:
                print('@', end='')
            else:
                print(' ', end='')
        print('')
    print('')
    
text = [
    'あいうえお',
    'かきくけこ',
    'さしすせそ'        
]

for linenum, line in enumerate(text):
    print("{}:{}".format(linenum + 1, line))

text = ['abc', 'def', 'hij']

for index, t in enumerate(text):
    print(str(index + 1) + ":" + t)
    