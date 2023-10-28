# int関数は文字列を整数に変換
seireki = int(input("2018年以降を入力してください: "))

# str関数は数値を文字列に変換
print("西暦" + str(seireki) + "年は、令和" + str(seireki - 2018) + "年")
