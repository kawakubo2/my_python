# -*- coding: utf-8 -*-

def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
# 高階関数(higher order function)---> 関数の引数として関数を取る、または戻り値として関数を返す関数を高階関数
for cm in map(to_cm, inches):
    print(cm)