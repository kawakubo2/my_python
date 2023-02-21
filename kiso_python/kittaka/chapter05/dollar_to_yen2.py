def dollar_to_yen(dollar=100, rate=105):
    return dollar * rate

yen=dollar_to_yen(dollar=100, rate=105)
print("為替レート: 105")
print(f"100ドルは{yen}円")

r = 100
d = 150
yen = dollar_to_yen(dollar=d, rate=r)
print(f"為替レート: {r}")
print(f"{d}ドルは{yen}円")

print("キーワード引数で呼び出す")
yen = dollar_to_yen(dollar=200, rate=100)
yen = dollar_to_yen(dollar=300)
yen = dollar_to_yen(rate=130)
yen = dollar_to_yen()
yen = dollar_to_yen(rate=130, dollar=150)