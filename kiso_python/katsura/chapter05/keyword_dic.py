def func(**dic):
    for key, value in dic.items():
        print(f"【{key}】:{value}")

func(green='緑', red='赤', blue='青')