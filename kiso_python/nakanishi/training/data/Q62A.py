from input_utils import input_int, input_float, input_int_range

# score = input_int_range(0, 100, "テストの点数")

n1 = input_float("整数1")
n2 = input_float("数値2")
x = input_float("数値")

if n1 < x < n2:
    print(f"{x}は{n1}より大きく{n2}より小さい")
else:
    print(f"{x}は{n1}以下または{n2}以上")