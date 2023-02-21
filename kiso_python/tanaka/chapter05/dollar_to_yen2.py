def dollar_to_yen(dollar=100, rate=105):
    return dollar * rate

dollar1 = 100
rate1 = 110

print("引数を全て指定した場合")
yen = dollar_to_yen(dollar1, rate1)
print(f"為替レート: {rate1}")
print(f"{dollar1}ドルは{yen}円")

print("レートを省略した場合")
yen = dollar_to_yen(dollar1)
print(f"為替レート: {rate1}")
print(f"{dollar1}ドルは{yen}円")

print("ドルを省略した場合")
yen = dollar_to_yen(rate=rate1) # ドルを省略したつもりがrateを省略したとみなされる
print(f"為替レート: {rate1}")
print(f"{dollar1}ドルは{yen}円")

print("引数の順序を入れ替える")
yen = dollar_to_yen(rate=rate1, dollar=dollar1) # ドルを省略したつもりがrateを省略したとみなされる
print(f"為替レート: {rate1}")
print(f"{dollar1}ドルは{yen}円")