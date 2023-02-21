def range_input(prompt, min=0, max=100):
    result = 0
    while True:
        try:
            result = int(input(prompt + ": "))
            if min <= result <= max:
                break
            print("{}～{}までの整数値を入力してください".format(min, max))
        except ValueError:
            print("整数値を入力してください")
    
    return result 

kokugo = range_input('国語', max=200)
sugaku = range_input('数学', max=200)
eigo   = range_input('英語', max=200)
print("国語: {}".format(kokugo))
print("数学: {}".format(sugaku))
print("英語: {}".format(eigo))
        