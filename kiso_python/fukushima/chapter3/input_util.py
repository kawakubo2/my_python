# -*- coding: utf-8 -*-

def input_range(min, max, prompt):
    while True:
        try:
            num = int(input(prompt + " : "))
        except ValueError:
            print("{}～{}を入力してください".format(min, max))
            continue
        if min <= num <= max:
            break
    return num
    