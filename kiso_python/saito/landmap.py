# -*- coding: utf-8 -*-

def printMap(lm):
    for row in lm:
        for elem in row:
            print(elem, end='')
        print()

landmap = [['森' for j in range(19)] for i in range(10)]

for i, row in enumerate(landmap): 
    for j, elem in enumerate(row):
        if i % 9 == 0 or j % 9 == 0:
            landmap[i][j] = '＋'
    

landmap[0][0] = landmap[0][18] = landmap[9][0] = landmap[9][18] = '町'
landmap[2][9] = '城'


printMap(landmap)


        
