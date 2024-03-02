def input_int(prompt):
    while True:
        try:
            num = int(input(f"{prompt}: "))
            break
        except:
            print("数値を入力してください")
    return num

def input_float(prompt):
    while True:
        try:
            num = float(input(f"{prompt}: "))
            break
        except:
            print("数値を入力してください")
    return num

def input_non_negative_float(prompt):
    while True:
        try:
            num = float(input(f"{prompt}: "))
            if num < 0: continue
            break
        except:
            print("数値を入力してください")
    return num

def input_int_range(min, max, prompt):
    if max <= min:
        raise Error("範囲の指定に誤りがあります")
    while True:
        try:
            num = int(input(f"{prompt}: "))
            if min <= num <= max:
                return num
        except:
            print("数値を入力してください")
    return num

def input_float_range(min, max, prompt):
    if max <= min:
        raise Error("範囲の指定に誤りがあります")
    while True:
        try:
            num = float(input(f"{prompt}: "))
            if min <= num <= max:
                return num
        except:
            print("数値を入力してください")
    return num