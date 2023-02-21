def dollar_to_yen(dollar, rate):
    return dollar * rate

yen = dollar_to_yen(100, 105)
print("為替レート: 105")
print(f"100ドルは{yen}円")

r = 100
d = 150
yen = dollar_to_yen(d, r)
print(f"為替レート: {r}")
print(f"{d}ドルは{yen}円")

yen = dollar_to_yen(dollar = 200, rate = 108)
print(f"200ドルは{yen}円")

yen = dollar_to_yen(rate = 108, dollar = 200)
print(f"200ドルは{yen}円")

