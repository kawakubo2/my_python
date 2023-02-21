# -*- coding: utf-8 -*-
    
dansu = int(input('段数'))

step = int(input('ステップ'))

def total_3d(dansu, step):
    return (sum([(n * (step * 2) + 1) ** 2 for n in range(dansu)]))

print(total_3d(dansu, step))
